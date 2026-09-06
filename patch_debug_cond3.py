import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            print("DEBUG COND TRUE NODE TYPE:", true_node.type if true_node else None, true_node.text if true_node else None)"""

replacement = """            print("DEBUG COND TRUE NODE TYPE:", true_node.type if true_node else None, true_node.text if true_node else None)
            if true_node:
                def print_tree(n, indent=0):
                    print(" " * indent + n.type)
                    for c in n.children: print_tree(c, indent + 2)
                print_tree(true_node)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
