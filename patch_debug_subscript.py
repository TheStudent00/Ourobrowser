import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """        elif node.type == 'subscript_expression':"""
replacement = """        elif node.type == 'subscript_expression':
            print("FOUND SUBSCRIPT", node.text)"""
content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
