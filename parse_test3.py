import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"void f() { cond ? a : b; }"
tree = parser.parse(src)
print(tree.root_node)
