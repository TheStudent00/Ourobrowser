import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"void f() { ((~raw) + 1u); }"
tree = parser.parse(src)
expr = tree.root_node.children[0].children[2].children[1].children[0]
print(expr.type, "is_named:", expr.is_named)
