import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            return self._create_node(SubscriptNode,
                value=self._map_node(val_node, source_bytes, scope) if val_node else self._create_node(IdentifierNode, name="unknown"),
                index=self._map_node(idx_node, source_bytes, scope) if idx_node else self._create_node(IdentifierNode, name="0")
            )"""

replacement = """            return self._create_node(SubscriptNode,
                value=self._map_node(val_node, source_bytes, scope) if val_node else self._create_node(IdentifierNode, name="unknown"),
                slice=self._map_node(idx_node, source_bytes, scope) if idx_node else self._create_node(IdentifierNode, name="0")
            )"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
