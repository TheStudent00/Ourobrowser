import tree_sitter_cpp as ts
from tree_sitter import Parser, Language

parser = Parser(Language(ts.language()))
src = b"class PLATFORM_EXPORT RuntimeCallStats { public: int x; };"
tree = parser.parse(src)
print(tree.root_node)
