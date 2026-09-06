import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """        elif node.type == 'binary_expression':
            left_node = node.child_by_field_name('left')"""

replacement = """        elif node.type == 'binary_expression':
            print("DEBUG BINARY:", node.text)
            left_node = node.child_by_field_name('left')"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
