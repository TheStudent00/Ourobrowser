import os
import sys
sys.path.append("~/Programming/Ourobrowser/Research/chromium_compilation")
from transpiler_loop import transpile_file
transpile_file("../../third_party/blink/renderer/bindings/core/v8/local_window_proxy.cc")
