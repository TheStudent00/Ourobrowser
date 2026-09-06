import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"void f() { uint64_t raw = words_[0]; }"
tree = parser.parse(src)
print(tree.root_node)
