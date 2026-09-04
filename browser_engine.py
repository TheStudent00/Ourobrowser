import html as html_escaping
import os
import sys
import re
from PyQt6.QtCore import QUrl, QBuffer, QIODevice, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QLineEdit, QToolButton, QMenu
)
from PyQt6.QtGui import QAction, QKeySequence, QShortcut, QIcon
from PyQt6.QtWebEngineCore import (
    QWebEngineUrlScheme,
    QWebEngineUrlSchemeHandler,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel

from bridge import PythonBridge


# ---------------------------------------------------------------------------
# THE WORKING NAMES.  Each is defined here and nowhere else, so changing one
# is a single edit.  Every one of them is Dee's to change.
# Stated in Planning/node_0_3_engine/node_0_1_scheme_handler/
# CORE_0_1_scheme_handler.md, section `## design`.
# ---------------------------------------------------------------------------

#: the name a <script type="text/python"> block calls to put HTML in its own
#: place.  Bound only while that block is running.
PAGE_EMIT_NAME = "emit"

#: the name that holds the absolute path of the file being served, so a page
#: can reach what sits beside it without carrying a machine-specific path.
PAGE_PATH_NAME = "page_path"

#: the name any python code calls to replace a named element's contents.
#: Bound once, to PythonBridge.set_html.
PAGE_PUSH_NAME = "set_html"

#: the attribute the click rewrite writes and the setup script reads.
PYTHON_CLICK_ATTRIBUTE = "data-python-onclick"

#: the page served when no page is named on the command line.
DEFAULT_PAGE = "test_page.html"


PYTHON_ONCLICK_PATTERN = re.compile(
    r'\bonclick=["\']python:(.*?)["\']',
    re.IGNORECASE
)


def rewrite_python_onclick(html_text):
    """Turn every `onclick="python:EXPR"` into `PYTHON_CLICK_ATTRIBUTE="EXPR"`.

    Nothing executable is written into the page.  The engine's own setup
    script carries ONE delegated click listener that reads the attribute and
    hands the expression to the bridge.

    This function is used in two places and defined in one: the scheme handler
    runs it over a page it is about to serve, and the bridge runs it over html
    that python pushes after first paint.  The bridge receives it as a
    constructor argument, so the bridge never imports this module.

    The rewrite it replaces wrote inline javascript through a raw-string
    template, and the backslashes in that template reached Chromium literally:

        <button onclick="if(window.pyBridge) { window.pyBridge.execute_python(
        \\'fetch_system_data()\\'); }">

    which Chromium refused with `Uncaught SyntaxError: Failed to execute
    'click' on 'HTMLElement': Invalid or unexpected token`, so no page could
    ever reach the bridge.
    """
    def one(match):
        expression = match.group(1)
        escaped = html_escaping.escape(expression, quote=True)
        return '%s="%s"' % (PYTHON_CLICK_ATTRIBUTE, escaped)

    return PYTHON_ONCLICK_PATTERN.sub(one, html_text)


def resolve_page_path(url_path):
    """Answer the file a request's path names.

    An absolute path is served as given; anything else is served relative to
    the working directory, which is what every page did before.  Absolute is
    tried first so that a page living outside this repo can be opened.
    """
    if not url_path:
        return DEFAULT_PAGE
    if os.path.isabs(url_path) and os.path.exists(url_path):
        return url_path
    stripped = url_path.lstrip('/')
    if not stripped:
        return DEFAULT_PAGE
    return stripped


def setup_script():
    """The engine's own script: the QWebChannel handshake, ONE delegated click
    listener, and the subscription that lets python fill an element.

    It is the only executable text the engine writes into a page.  The click
    listener is delegated from `document`, so an element that arrives later
    through `set_html` is already live and nothing re-wires it.
    """
    return """
        <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
        <script>
        (function () {
            var ATTR = "%s";
            document.addEventListener("click", function (ev) {
                var node = null;
                if (ev.target && ev.target.closest) {
                    node = ev.target.closest("[" + ATTR + "]");
                }
                if (node && window.pyBridge) {
                    window.pyBridge.execute_python(node.getAttribute(ATTR));
                }
            });
            document.addEventListener("DOMContentLoaded", function () {
                new QWebChannel(qt.webChannelTransport, function (channel) {
                    window.pyBridge = channel.objects.pyBridge;
                    window.pyBridge.html_pushed.connect(function (target, markup) {
                        var el = document.getElementById(target);
                        if (el) {
                            el.innerHTML = markup;
                        }
                    });
                });
            });
        })();
        </script>
        """ % PYTHON_CLICK_ATTRIBUTE


class OurobrowserSchemeHandler(QWebEngineUrlSchemeHandler):
    """
    Custom URL Scheme Handler that intercepts HTML loading,
    strips standard JS, executes embedded Python scripts, and
    rewrites python: onclick handlers to bridge calls.

    Node: ourobrowser.root.engine.scheme_handler
    (Planning/node_0_3_engine/node_0_1_scheme_handler/
    CORE_0_1_scheme_handler.md).
    """
    def __init__(self, context, parent=None):
        super().__init__(parent)
        self.context = context

    def requestStarted(self, request):
        url = request.requestUrl()
        # Request should look like ourobrowser://local/test_page.html
        path = resolve_page_path(url.path())

        try:
            with open(path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except FileNotFoundError:
            print(f"[Engine] File not found: {path}", file=sys.stderr)
            request.fail(request.Error.UrlNotFound)
            return

        absolute = os.path.abspath(path)

        # 1. Extract and execute <script type="text/python">.  A block may EMIT
        #    html in place of itself by calling PAGE_EMIT_NAME; a block that
        #    emits nothing is replaced by the empty string, exactly as before.
        python_script_pattern = re.compile(
            r'<script\s+type=["\']text/python["\']>(.*?)</script>',
            re.IGNORECASE | re.DOTALL
        )

        def execute_and_replace(match):
            code = match.group(1)
            print("[Engine] Executing embedded Python script...")
            emitted = []

            def collect(markup):
                emitted.append(str(markup))

            had_emit = PAGE_EMIT_NAME in self.context
            previous_emit = self.context.get(PAGE_EMIT_NAME)
            self.context[PAGE_EMIT_NAME] = collect
            self.context[PAGE_PATH_NAME] = absolute
            try:
                exec(code, self.context, self.context)
            except Exception as e:
                print(f"[Engine] Error in embedded Python script: {e}", file=sys.stderr)
            finally:
                if had_emit:
                    self.context[PAGE_EMIT_NAME] = previous_emit
                else:
                    self.context.pop(PAGE_EMIT_NAME, None)
            if emitted:
                print("[Engine] Block emitted %d characters of HTML"
                      % sum(len(x) for x in emitted))
            return "".join(emitted)

        html_content = python_script_pattern.sub(execute_and_replace, html_content)

        # 2. Strip all other standard <script> tags to disable JS completely.
        #    This runs AFTER the emission, so html a block emits cannot smuggle
        #    javascript in.
        standard_script_pattern = re.compile(
            r'<script\b(?![^>]*type=["\']text/python["\'])[^>]*>.*?</script>',
            re.IGNORECASE | re.DOTALL
        )
        html_content = standard_script_pattern.sub("", html_content)

        # 3. Rewrite onclick="python:..." into the bridge's wire attribute.
        #    This runs AFTER the emission, so html a block emitted gets its
        #    python: handlers rewritten like any other.
        html_content = rewrite_python_onclick(html_content)

        # 4. Inject the engine's own setup script at the end of the head
        injection_script = setup_script()
        if "</head>" in html_content:
            html_content = html_content.replace("</head>", injection_script + "</head>")
        else:
            html_content = injection_script + html_content

        # Send the modified HTML back to the browser engine
        buffer = QBuffer(request)
        buffer.setData(html_content.encode('utf-8'))
        buffer.open(QIODevice.OpenModeFlag.ReadOnly)
        request.reply(b"text/html", buffer)


class OurobrowserWindow(QMainWindow):
    def __init__(self, start_page=None):
        super().__init__()
        self.setWindowTitle("Ourobrowser (Python Native)")
        self.setWindowIcon(QIcon("ouroboros.svg"))
        self.resize(1024, 768)

        self.start_page = start_page or DEFAULT_PAGE

        # Shared execution context for the Python scripts and bridge
        self.python_context = {}

        # Set up the web view
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Build UI (Toolbar, Address bar, etc.)
        self.setup_ui()

        # Set up QWebChannel and Python Bridge.  The engine hands the bridge
        # its own click rewrite, so html python pushes after first paint is
        # rewritten by the same function that rewrites a served page.
        self.channel = QWebChannel()
        self.bridge = PythonBridge(
            context=self.python_context,
            rewriter=rewrite_python_onclick,
        )
        self.channel.registerObject("pyBridge", self.bridge)
        self.browser.page().setWebChannel(self.channel)

        # The one name page code calls to fill an element.
        self.python_context[PAGE_PUSH_NAME] = self.bridge.set_html

        # Set up the custom URL scheme handler
        self.scheme_handler = OurobrowserSchemeHandler(
            context=self.python_context,
            parent=self.browser.page().profile()
        )
        self.browser.page().profile().installUrlSchemeHandler(b"ourobrowser", self.scheme_handler)

        # Developer Tools Setup
        self.devtools_window = None
        self.shortcut_dev = QShortcut(QKeySequence("F12"), self)
        self.shortcut_dev.activated.connect(self.toggle_devtools)

        # Load the starting page via our custom scheme
        self.browser.setUrl(QUrl("ourobrowser://local/" + self.start_page))

    def setup_ui(self):
        # Navigation Toolbar
        self.toolbar = QToolBar("Navigation")
        self.addToolBar(self.toolbar)

        # Back / Forward / Reload
        back_action = QAction("← Back", self)
        back_action.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_action)

        forward_action = QAction("Forward →", self)
        forward_action.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_action)

        reload_action = QAction("↻ Reload", self)
        reload_action.triggered.connect(self.browser.reload)
        self.toolbar.addAction(reload_action)

        self.toolbar.addSeparator()

        # Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)

        # Update address bar when URL changes
        self.browser.urlChanged.connect(self.update_url_bar)

        self.toolbar.addSeparator()

        # Hamburger Menu
        hamburger_menu = QMenu(self)
        dev_tools_action = hamburger_menu.addAction("Developer Tools (F12)")
        dev_tools_action.triggered.connect(self.toggle_devtools)

        hamburger_btn = QToolButton()
        hamburger_btn.setText("≡ Options")
        hamburger_btn.setMenu(hamburger_menu)
        hamburger_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolbar.addWidget(hamburger_btn)

        # Bookmarks Bar (Second Toolbar on a new line)
        self.addToolBarBreak()
        self.bookmarks_bar = QToolBar("Bookmarks")
        self.addToolBar(self.bookmarks_bar)

        test_page_action = QAction("⭐ Test Page", self)
        test_page_action.triggered.connect(lambda: self.browser.setUrl(QUrl("ourobrowser://local/test_page.html")))
        self.bookmarks_bar.addAction(test_page_action)

    def navigate_to_url(self):
        url_text = self.url_bar.text()
        # Ensure it always prepends our custom scheme if it's missing it
        if not url_text.startswith("http") and not url_text.startswith("ourobrowser://"):
            url_text = "ourobrowser://local/" + url_text
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def toggle_devtools(self):
        if self.devtools_window is None:
            self.devtools_window = QMainWindow()
            self.devtools_view = QWebEngineView()
            self.devtools_window.setCentralWidget(self.devtools_view)
            self.devtools_window.setWindowTitle("Developer Tools")
            self.devtools_window.resize(800, 600)
            self.browser.page().setDevToolsPage(self.devtools_view.page())

        if self.devtools_window.isVisible():
            self.devtools_window.hide()
        else:
            self.devtools_window.show()


def main():
    # Register the custom URL scheme before creating QApplication
    scheme = QWebEngineUrlScheme(b"ourobrowser")
    scheme.setSyntax(QWebEngineUrlScheme.Syntax.HostAndPort)

    scheme.setFlags(
        QWebEngineUrlScheme.Flag.SecureScheme |
        QWebEngineUrlScheme.Flag.LocalScheme |
        QWebEngineUrlScheme.Flag.LocalAccessAllowed
    )
    QWebEngineUrlScheme.registerScheme(scheme)

    start_page = DEFAULT_PAGE
    if len(sys.argv) > 1:
        start_page = sys.argv[1]

    app = QApplication(sys.argv[:1])
    window = OurobrowserWindow(start_page=start_page)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
