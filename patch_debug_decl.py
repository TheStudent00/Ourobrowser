import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            right = self._map_node(right_node, source_bytes, scope) if right_node else None"""
replacement = """            if right_node: print(f"DEBUG decl right_node: {right_node.type} -> {self._get_text(right_node, source_bytes)}")
            right = self._map_node(right_node, source_bytes, scope) if right_node else None"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
