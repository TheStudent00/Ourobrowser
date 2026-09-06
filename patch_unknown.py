import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            raw_name = "unknown"
            if decl_node:
                id_node = next((c for c in decl_node.named_children if c.type in ('identifier', 'field_identifier')), None)
                if id_node: raw_name = self._get_text(id_node, source_bytes)"""

replacement = """            raw_name = "unknown"
            if decl_node:
                # Recursively find the innermost identifier or qualified_identifier
                def get_id(n):
                    if not n: return None
                    if n.type in ('identifier', 'field_identifier', 'qualified_identifier', 'destructor_name', 'operator_name'):
                        return n
                    for c in n.named_children:
                        res = get_id(c)
                        if res: return res
                    return None
                
                id_node = get_id(decl_node)
                if id_node: raw_name = self._get_text(id_node, source_bytes)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
