import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """        # Fallback to children
        if node.child_count > 0:
            for c in node.named_children:
                m = self._map_node(c, source_bytes, scope)
                if m: return m
                
        return self._create_node(LiteralNode, value=None)"""

replacement = """        # Fallback to children
        if node.child_count > 0:
            for c in node.named_children:
                m = self._map_node(c, source_bytes, scope)
                if m: return m
                
        print(f"DEBUG FALLBACK None for node type: {node.type}")
        return self._create_node(LiteralNode, value=None)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
