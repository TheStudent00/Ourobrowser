import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target_imports = "from pseudocoup.core.ur_ast import ("
replacement_imports = target_imports + "\n    NamespaceNode,"
content = content.replace(target_imports, replacement_imports)

target = "    def visit_ModuleNode(self, node: ModuleNode) -> str:"
replacement = """    def visit_NamespaceNode(self, node: NamespaceNode) -> str:
        out = [f"namespace {node.name} {{"]
        self.push_scope()
        for stmt in node.body:
            stmt_str = self.generate(stmt)
            if stmt_str:
                out.append(self.indent(stmt_str))
        self.pop_scope()
        out.append(f"}} // namespace {node.name}")
        return "\\n".join(out)

    def visit_ModuleNode(self, node: ModuleNode) -> str:"""

content = content.replace(target, replacement)
with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
