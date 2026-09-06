import re

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'r') as f:
    content = f.read()

target = """class UnaryOpNode(URNode):
    def __init__(self, operator: str, operand: 'URNode'):
        super().__init__()
        self.operator = operator
        self.operand = operand"""

replacement = target + """

class SubscriptNode(URNode):
    def __init__(self, value: 'URNode', index: 'URNode'):
        super().__init__()
        self.value = value
        self.index = index

class ConditionalNode(URNode):
    def __init__(self, condition: 'URNode', true_expr: 'URNode', false_expr: 'URNode'):
        super().__init__()
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'w') as f:
    f.write(content)
