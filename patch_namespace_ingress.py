import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target_imports = "from pseudocoup.core.ur_ast import ("
replacement_imports = target_imports + "\n    NamespaceNode,"
content = content.replace(target_imports, replacement_imports)

target = "        elif node.type == 'declaration':"
replacement = """        elif node.type == 'namespace_definition':
            name_node = node.child_by_field_name('name')
            name = self._get_text(name_node, source_bytes) if name_node else "Unknown"
            
            body_node = node.child_by_field_name('body')
            body = []
            if body_node:
                for c in body_node.named_children:
                    m = self._map_node(c, source_bytes, scope)
                    if isinstance(m, list): body.extend(m)
                    elif m: body.append(m)
            return self._create_node(NamespaceNode, name=name, body=body)

        elif node.type == 'declaration':"""

content = content.replace(target, replacement)
with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
