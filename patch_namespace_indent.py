import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = """    def visit_NamespaceNode(self, node: NamespaceNode) -> str:
        out = [f"namespace {node.name} {{"]
        self.push_scope()
        for stmt in node.body:
            stmt_str = self.generate(stmt)
            if stmt_str:
                out.append(f"{self._indent()}{stmt_str}")
        self.pop_scope()
        out.append(f"}} // namespace {node.name}")
        return "\\n".join(out)"""

replacement = """    def visit_NamespaceNode(self, node: NamespaceNode) -> str:
        out = [f"namespace {node.name} {{"]
        self.push_scope()
        self.indent_level += 1
        for stmt in node.body:
            stmt_str = self.generate(stmt)
            if stmt_str:
                if isinstance(stmt, (AssignmentNode, ReturnNode)):
                    out.append(f"{self._indent()}{stmt_str};")
                elif isinstance(stmt, (IfNode, WhileNode, ForNode, TryCatchNode)):
                    out.append(stmt_str)
                else:
                    if not stmt_str.endswith(";") and not stmt_str.endswith("}"):
                        stmt_str += ";"
                    out.append(f"{self._indent()}{stmt_str}")
        self.indent_level -= 1
        self.pop_scope()
        out.append(f"}} // namespace {node.name}")
        return "\\n".join(out)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
