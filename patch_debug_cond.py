import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = """    def visit_ConditionalNode(self, node: ConditionalNode) -> str:
        return f"({self.generate(node.condition)} ? {self.generate(node.true_expr)} : {self.generate(node.false_expr)})\""""

replacement = """    def visit_ConditionalNode(self, node: ConditionalNode) -> str:
        print(f"DEBUG COND condition: {node.condition}")
        print(f"DEBUG COND true_expr: {node.true_expr}")
        print(f"DEBUG COND false_expr: {node.false_expr}")
        return f"({self.generate(node.condition)} ? {self.generate(node.true_expr)} : {self.generate(node.false_expr)})\""""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
