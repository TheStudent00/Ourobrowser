import sys
from PyQt6.QtCore import QObject, pyqtSlot

class PythonBridge(QObject):
    """
    The communication layer that bridges HTML DOM actions directly to native Python functions.
    It exposes a slot to the QWebChannel that executes Python code in a shared context.
    """
    def __init__(self, context=None):
        super().__init__()
        self.context = context if context is not None else {}

    @pyqtSlot(str)
    def execute_python(self, command):
        """
        Executes a python command originating from the HTML DOM (e.g., onclick="python:my_func()").
        """
        print(f"[Bridge] Executing Python command: {command}")
        try:
            # We use exec to support full function calls and statements
            exec(command, self.context, self.context)
        except Exception as e:
            print(f"[Bridge] Error executing python command '{command}': {e}", file=sys.stderr)
