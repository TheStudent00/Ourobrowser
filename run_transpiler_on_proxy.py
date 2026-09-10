import os
import sys
sys.path.append("PUBLIC/Ourobrowser/Research/chromium_compilation")
import transpiler_loop
transpiler_loop.CHROMIUM_SRC = "chromium_src/src"
transpiler_loop.PC_V3_CLI = "PUBLIC/Ourobrowser/Tools/PCv3.1/pseudocoup/cli.py"
transpiler_loop.PC_V3_PYTHONPATH = "PUBLIC/Ourobrowser/Tools/PCv3.1"
transpiler_loop.transpile_file("../../third_party/blink/renderer/bindings/core/v8/local_window_proxy.cc")
