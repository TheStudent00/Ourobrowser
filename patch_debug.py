import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """        elif node.type == 'subscript_expression':
            val_node = node.child_by_field_name('argument')"""

replacement = """        elif node.type == 'subscript_expression':
            print(f"DEBUG subscript_expression: {node.text}")
            val_node = node.child_by_field_name('argument')"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
