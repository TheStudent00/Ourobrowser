import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = "out.append(self.indent(stmt_str))"
replacement = 'out.append(f"{self._indent()}{stmt_str}")'

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
