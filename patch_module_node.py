import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = """    def visit_ModuleNode(self, node: ModuleNode) -> str:
        self.push_scope()
        lines = [
            "#include <iostream>",
            "#include <string>",
            "#include <vector>",
            "#include <unordered_map>",
            "#include <any>",
            "#include <stdexcept>",
            ""
        ]
        for stmt in node.body:"""

replacement = """    def visit_ModuleNode(self, node: ModuleNode) -> str:
        self.push_scope()
        lines = []
        for stmt in node.body:"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
