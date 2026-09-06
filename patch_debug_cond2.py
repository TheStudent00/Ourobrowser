import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            true_node = node.child_by_field_name('consequence')"""

replacement = """            true_node = node.child_by_field_name('consequence')
            print("DEBUG COND TRUE NODE TYPE:", true_node.type if true_node else None, true_node.text if true_node else None)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
