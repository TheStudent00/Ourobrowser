import tree_sitter_cpp as ts
from tree_sitter import Language, Parser
parser = Parser(Language(ts.language()))
src = b"class A { explicit A(); };"
tree = parser.parse(src)
decl = tree.root_node.children[0].children[2].children[1]
print("type:", decl.type)
print("declarator field:", decl.child_by_field_name('declarator'))
