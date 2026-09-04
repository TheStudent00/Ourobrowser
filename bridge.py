import sys
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot


def _identity(html):
    """the default rewriter: hand the html back unchanged.

    The engine passes its own `rewrite_python_onclick` in when it builds
    the bridge (see Planning/node_0_4_bridge/node_0_0_web_channel/
    CORE_0_0_web_channel.md, "The rewrite is INJECTED, not imported").
    """
    return html


class PythonBridge(QObject):
    """
    The communication layer that bridges HTML DOM actions directly to native
    Python functions, and carries Python's answer back into the DOM.

    Node: ourobrowser.root.bridge.web_channel
    (Planning/node_0_4_bridge/node_0_0_web_channel/CORE_0_0_web_channel.md).

    Two directions:
      DOM -> Python   `execute_python`, a slot the page's setup script calls.
                      Unchanged: it exec's in the shared context and discards
                      the return value.
      Python -> DOM   `html_pushed`, a Qt signal. QWebChannel publishes a
                      registered object's signals to the page, so the setup
                      script subscribes to it in one line and no new transport
                      is invented.
    """

    # WORKING NAME, defined here and nowhere else. Two strings: the id of the
    # element to fill, and the html to put in it.
    html_pushed = pyqtSignal(str, str)

    def __init__(self, context=None, rewriter=None):
        super().__init__()
        self.context = context if context is not None else {}
        self.rewriter = rewriter if rewriter is not None else _identity

    @pyqtSlot(str)
    def execute_python(self, command):
        """
        Executes a python command originating from the HTML DOM (e.g.
        onclick="python:my_func()").
        """
        print(f"[Bridge] Executing Python command: {command}")
        try:
            # We use exec to support full function calls and statements
            exec(command, self.context, self.context)
        except Exception as e:
            print(f"[Bridge] Error executing python command '{command}': {e}", file=sys.stderr)

    def set_html(self, target, html):
        """
        Replaces the contents of the element whose id is `target` with `html`.

        The html is put through the engine's click rewrite first, because html
        pushed after first paint never passes through the scheme handler and
        would otherwise carry `python:` handlers nothing had rewritten. It is a
        method rather than a bare signal emission so that a caller cannot
        forget the rewrite.
        """
        text = self.rewriter(html)
        print(f"[Bridge] Pushing {len(text)} characters of HTML into '{target}'")
        self.html_pushed.emit(str(target), text)
