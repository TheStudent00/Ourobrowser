import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"void f() { uint64_t raw; raw = IsNegative() ? ((~raw) + 1u) : raw; }"
tree = parser.parse(src)
print(tree.root_node)
