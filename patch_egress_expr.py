import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

# Add missing node imports
target_imports = "from pseudocoup.core.ur_ast import ("
replacement_imports = target_imports + "\n    SubscriptNode, ConditionalNode,"
content = content.replace(target_imports, replacement_imports)

# Add visit methods
target_methods = """    def visit_UnaryOpNode(self, node):
        return f"{node.operator}{self.generate(node.operand)}"
"""

replacement_methods = target_methods + """
    def visit_SubscriptNode(self, node):
        return f"{self.generate(node.value)}[{self.generate(node.index)}]"

    def visit_ConditionalNode(self, node):
        return f"({self.generate(node.condition)} ? {self.generate(node.true_expr)} : {self.generate(node.false_expr)})"
"""
content = content.replace(target_methods, replacement_methods)

# Fix visit_FunctionDefNode to use node.return_type instead of node.metadata.get
target_ret = "return_type = self.map_type(node.metadata.get('return_type', 'void'), \"return\")"
replacement_ret = "return_type = self.map_type(node.return_type or 'void', \"return\")"
content = content.replace(target_ret, replacement_ret)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
