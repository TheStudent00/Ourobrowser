import re

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'r') as f:
    content = f.read()

target = """class CastNode(URNode):
    def __init__(self, target_type=None, value=None, **kwargs):
        super().__init__(**kwargs)
        self.target_type = target_type
        self.value = value"""

replacement = target + """

class SubscriptNode(URNode):
    def __init__(self, value: 'URNode' = None, index: 'URNode' = None, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.index = index

class ConditionalNode(URNode):
    def __init__(self, condition: 'URNode' = None, true_expr: 'URNode' = None, false_expr: 'URNode' = None, **kwargs):
        super().__init__(**kwargs)
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/core/ur_ast.py', 'w') as f:
    f.write(content)
