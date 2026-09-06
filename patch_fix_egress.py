import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = """    def visit_SubscriptNode(self, node):
        return f"{self.generate(node.value)}[{self.generate(node.index)}]"

"""

content = content.replace(target, "")

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
