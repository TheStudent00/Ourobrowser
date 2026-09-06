import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """        elif node.type == 'subscript_expression':
            val_node = node.child_by_field_name('argument')
            idx_node = node.child_by_field_name('index')
            if not val_node or not idx_node:
                # Tree-sitter cpp subscript_expression doesn't always use named fields, fallback to children
                val_node = node.children[0] if len(node.children) > 0 else None
                idx_node = node.children[2] if len(node.children) > 2 else None
            return self._create_node(SubscriptNode,
                value=self._map_node(val_node, source_bytes, scope) if val_node else self._create_node(IdentifierNode, name="unknown"),
                index=self._map_node(idx_node, source_bytes, scope) if idx_node else self._create_node(IdentifierNode, name="0")
            )"""

replacement = """        elif node.type == 'subscript_expression':
            val_node = node.child_by_field_name('argument')
            indices_node = node.child_by_field_name('indices')
            idx_node = None
            if indices_node and indices_node.type == 'subscript_argument_list':
                # indices_node has '[', expr, ']'
                for c in indices_node.named_children:
                    idx_node = c
                    break
            
            return self._create_node(SubscriptNode,
                value=self._map_node(val_node, source_bytes, scope) if val_node else self._create_node(IdentifierNode, name="unknown"),
                index=self._map_node(idx_node, source_bytes, scope) if idx_node else self._create_node(IdentifierNode, name="0")
            )"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
