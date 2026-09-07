import tree_sitter_cpp as ts
from tree_sitter import Language, Parser
parser = Parser(Language(ts.language()))
src = b"class A { A(const A&) = delete; };"
tree = parser.parse(src)
def print_node(node, indent=0):
    print("  "*indent + node.type + (" ("+node.type+")" if node.is_named else ""))
    for child in node.children:
        print_node(child, indent+1)
print_node(tree.root_node)
