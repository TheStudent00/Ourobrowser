import re

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'r') as f:
    content = f.read()

target = """class SubscriptNode(URNode):"""

replacement = """class NamespaceNode(URNode):
    def __init__(self, name: str, body: list):
        super().__init__()
        self.name = name
        self.body = body

class SubscriptNode(URNode):"""

content = content.replace(target, replacement)
with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'w') as f:
    f.write(content)
