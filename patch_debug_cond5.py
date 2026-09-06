import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """                print("DEBUG PAREN IS_NAMED:", true_node.is_named)"""

replacement = """                print("DEBUG PAREN IS_NAMED:", true_node.is_named)
                print("DEBUG PAREN NAMED CHILDREN:", [c.type for c in true_node.named_children])"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
