import tree_sitter_cpp as ts
from tree_sitter import Language, Parser

parser = Parser(Language(ts.language()))

src = b"void foo() { if (auto* iframe = DynamicTo<HTMLIFrameElement>(*element)) {} }"
tree = parser.parse(src)
decl = tree.root_node.children[0].children[2].children[1].children[1].children[1]
print("DECL:", decl.type)
print("DECL value child:", decl.child_by_field_name('value'))
print("DECL declarator child:", decl.child_by_field_name('declarator'))
