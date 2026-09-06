import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

# Add parenthesized_expression and template_function
target = "        elif node.type == 'call_expression':"

replacement = """        elif node.type == 'parenthesized_expression':
            if len(node.named_children) > 0:
                return self._map_node(node.named_children[0], source_bytes, scope)
            return None
            
        elif node.type == 'template_function':
            return self._create_node(IdentifierNode, name=self._get_text(node, source_bytes))

        elif node.type == 'call_expression':"""

content = content.replace(target, replacement)

# Clean up my debug prints from earlier inside conditional_expression
target_debug = """            print("DEBUG COND TRUE NODE TYPE:", true_node.type if true_node else None, true_node.text if true_node else None)
            if true_node:
                def print_tree(n, indent=0):
                    print(" " * indent + n.type)
                    for c in n.children: print_tree(c, indent + 2)
                print_tree(true_node)
                print("DEBUG PAREN IS_NAMED:", true_node.is_named)
                print("DEBUG PAREN NAMED CHILDREN:", [c.type for c in true_node.named_children])"""

content = content.replace(target_debug, "")
content = content.replace('print("DEBUG BINARY:", node.text)', "")

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
