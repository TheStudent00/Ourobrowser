import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = "        elif node.type == 'call_expression':"

replacement = """        elif node.type == 'subscript_expression':
            val_node = node.child_by_field_name('argument')
            indices_node = node.child_by_field_name('indices')
            idx_node = None
            if indices_node and indices_node.type == 'subscript_argument_list':
                for c in indices_node.named_children:
                    idx_node = c
                    break
            
            return self._create_node(SubscriptNode,
                value=self._map_node(val_node, source_bytes, scope) if val_node else self._create_node(IdentifierNode, name="unknown"),
                index=self._map_node(idx_node, source_bytes, scope) if idx_node else self._create_node(IdentifierNode, name="0")
            )

        elif node.type == 'conditional_expression':
            cond_node = node.child_by_field_name('condition')
            true_node = node.child_by_field_name('consequence')
            false_node = node.child_by_field_name('alternative')
            return self._create_node(ConditionalNode,
                condition=self._map_node(cond_node, source_bytes, scope) if cond_node else self._create_node(IdentifierNode, name="true"),
                true_expr=self._map_node(true_node, source_bytes, scope) if true_node else self._create_node(IdentifierNode, name="unknown"),
                false_expr=self._map_node(false_node, source_bytes, scope) if false_node else self._create_node(IdentifierNode, name="unknown")
            )

        elif node.type == 'call_expression':"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
