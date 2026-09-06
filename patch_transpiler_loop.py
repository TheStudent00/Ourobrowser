import re

with open('Research/chromium_compilation/transpiler_loop.py', 'r') as f:
    content = f.read()

target = """    with open(abs_path, 'r') as f:
        content = f.read()
    
    content = content.replace('#include "v8/include/v8.h"', '#include <Python.h>')
    content = content.replace('#include "v8.h"', '#include <Python.h>')
    content = content.replace(' PLATFORM_EXPORT ', ' ')
    content = content.replace(' CORE_EXPORT ', ' ')
    content = content.replace(' BLINK_PLATFORM_EXPORT ', ' ')
    content = content.replace('}  // namespace blink', '// }  // namespace blink')
    
    with open(abs_path, 'w') as f:
        f.write(content)"""

replacement = """    with open(abs_path, 'r') as f:
        content = f.read()
        
    includes = []
    for line in content.split('\\n'):
        if line.strip().startswith('#'):
            includes.append(line)
    
    content = content.replace('#include "v8/include/v8.h"', '#include <Python.h>')
    content = content.replace('#include "v8.h"', '#include <Python.h>')
    content = content.replace(' PLATFORM_EXPORT ', ' ')
    content = content.replace(' CORE_EXPORT ', ' ')
    content = content.replace(' BLINK_PLATFORM_EXPORT ', ' ')
    
    with open(abs_path, 'w') as f:
        f.write(content)"""

content = content.replace(target, replacement)

target2 = """    out_ext = ".cpp"
    out_path = abs_path.rsplit('.', 1)[0] + out_ext
    if os.path.exists(out_path) and out_path != abs_path:
        shutil.move(out_path, abs_path)"""

replacement2 = """    out_ext = ".cpp"
    out_path = abs_path.rsplit('.', 1)[0] + out_ext
    if os.path.exists(out_path) and out_path != abs_path:
        with open(out_path, 'r') as f:
            out_content = f.read()
        with open(abs_path, 'w') as f:
            f.write('\\n'.join(includes) + '\\n\\n' + out_content)
        os.remove(out_path)"""

content = content.replace(target2, replacement2)

with open('Research/chromium_compilation/transpiler_loop.py', 'w') as f:
    f.write(content)
