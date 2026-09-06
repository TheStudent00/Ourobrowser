import re

with open('Research/chromium_compilation/transpiler_loop.py', 'r') as f:
    content = f.read()

target = """    for line in content.split('\\n'):
        if line.strip().startswith('#'):
            includes.append(line)"""

replacement = """    for line in content.split('\\n'):
        if line.strip().startswith('#'):
            line = line.replace('#include "v8/include/v8.h"', '#include <Python.h>')
            line = line.replace('#include "v8.h"', '#include <Python.h>')
            includes.append(line)"""

content = content.replace(target, replacement)

with open('Research/chromium_compilation/transpiler_loop.py', 'w') as f:
    f.write(content)
