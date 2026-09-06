import re

with open('Research/chromium_compilation/transpiler_loop.py', 'r') as f:
    content = f.read()

target = """    content = content.replace('#include "v8.h"', '#include <Python.h>')"""

replacement = """    content = content.replace('#include "v8.h"', '#include <Python.h>')
    content = content.replace(' PLATFORM_EXPORT ', ' ')
    content = content.replace(' CORE_EXPORT ', ' ')
    content = content.replace(' BLINK_PLATFORM_EXPORT ', ' ')"""

content = content.replace(target, replacement)

with open('Research/chromium_compilation/transpiler_loop.py', 'w') as f:
    f.write(content)
