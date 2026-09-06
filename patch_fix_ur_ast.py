import re

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'r') as f:
    content = f.read()

# Remove the duplicate SubscriptNode
target = """class SubscriptNode(URNode):
    def __init__(self, value: 'URNode' = None, index: 'URNode' = None, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.index = index"""

content = content.replace(target, "")

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'w') as f:
    f.write(content)
