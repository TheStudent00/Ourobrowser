import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"void f() { uint64_t raw; raw = IsNegative() ? ((~raw) + 1u) : raw; }"
tree = parser.parse(src)

def find_paren(node):
    if node.type == 'parenthesized_expression':
        print(f"parenthesized_expression text: {node.text}")
        print(f"named_children: {[c.type for c in node.named_children]}")
    for c in node.children:
        find_paren(c)

find_paren(tree.root_node)
