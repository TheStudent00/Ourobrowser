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


class OurobrowserSchemeHandler(QWebEngineUrlSchemeHandler):
    """
    Custom URL Scheme Handler that intercepts HTML loading,
    strips standard JS, executes embedded Python scripts, and
    rewrites python: onclick handlers to bridge calls.
    """
    def __init__(self, context, parent=None):
        super().__init__(parent)
        self.context = context

    def requestStarted(self, request):
        url = request.requestUrl()
        # Request should look like ourobrowser://local/test_page.html
        path = url.path().lstrip('/')
        if not path:
            path = "test_page.html"
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html_content = f.read()
        except FileNotFoundError:
            print(f"[Engine] File not found: {path}", file=sys.stderr)
            request.fail(request.Error.UrlNotFound)
            return

        # 1. Extract and execute <script type="text/python">
        python_script_pattern = re.compile(
            r'<script\s+type=["\']text/python["\']>(.*?)</script>',
            re.IGNORECASE | re.DOTALL
        )
        
        def execute_and_remove(match):
            code = match.group(1)
            print("[Engine] Executing embedded Python script...")
            try:
                exec(code, self.context, self.context)
            except Exception as e:
                print(f"[Engine] Error in embedded Python script: {e}", file=sys.stderr)
            return "" # Remove the python script from the HTML passed to Chromium

        html_content = python_script_pattern.sub(execute_and_remove, html_content)
        
        # 2. Strip all other standard <script> tags to disable JS completely
        standard_script_pattern = re.compile(
            r'<script\b(?![^>]*type=["\']text/python["\'])[^>]*>.*?</script>',
            re.IGNORECASE | re.DOTALL
        )
        html_content = standard_script_pattern.sub("", html_content)

        # 3. Rewrite onclick="python:..." to bridge calls
        onclick_pattern = re.compile(
            r'\bonclick=["\']python:(.*?)["\']',
            re.IGNORECASE
        )
        # We inject a tiny JS shim solely to send the command over QWebChannel
        replacement = r'onclick="if(window.pyBridge) { window.pyBridge.execute_python(\'\1\'); }"'
        html_content = onclick_pattern.sub(replacement, html_content)
        
        # 4. Inject QWebChannel setup script at the end of the head or body
        injection_script = """
        <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                new QWebChannel(qt.webChannelTransport, function(channel) {
                    window.pyBridge = channel.objects.pyBridge;
                });
            });
        </script>
        """
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
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ourobrowser (Python Native)")
        self.setWindowIcon(QIcon("ouroboros.svg"))
        self.resize(1024, 768)

        # Shared execution context for the Python scripts and bridge
        self.python_context = {}

        # Set up the web view
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Build UI (Toolbar, Address bar, etc.)
        self.setup_ui()

        # Set up QWebChannel and Python Bridge
        self.channel = QWebChannel()
        self.bridge = PythonBridge(context=self.python_context)
        self.channel.registerObject("pyBridge", self.bridge)
        self.browser.page().setWebChannel(self.channel)

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

        # Load the test page via our custom scheme
        self.browser.setUrl(QUrl("ourobrowser://local/test_page.html"))

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

    app = QApplication(sys.argv)
    window = OurobrowserWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
