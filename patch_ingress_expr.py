import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

# Add imports for new nodes
target_imports = "from pseudocoup.core.ur_ast import ("
replacement_imports = target_imports + "\n    SubscriptNode, ConditionalNode,"
content = content.replace(target_imports, replacement_imports)

# Add parsing for subscript_expression
target_parse = """        elif node.type == 'cast_expression':
            type_node = node.child_by_field_name('type')
            value_node = node.child_by_field_name('value')
            return self._create_node(CastNode, 
                target_type=self._get_text(type_node, source_bytes) if type_node else "Any",
                value=self._map_node(value_node, source_bytes, scope) if value_node else self._create_node(IdentifierNode, name="unknown")
            )"""

replacement_parse = target_parse + """
        elif node.type == 'subscript_expression':
            val_node = node.child_by_field_name('argument')
            idx_node = node.child_by_field_name('index')
            if not val_node or not idx_node:
                # Tree-sitter cpp subscript_expression doesn't always use named fields, fallback to children
                val_node = node.children[0] if len(node.children) > 0 else None
                idx_node = node.children[2] if len(node.children) > 2 else None
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
            )"""

content = content.replace(target_parse, replacement_parse)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
