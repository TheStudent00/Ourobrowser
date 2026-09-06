import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """                print_tree(true_node)"""

replacement = """                print_tree(true_node)
                print("DEBUG PAREN IS_NAMED:", true_node.is_named)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
