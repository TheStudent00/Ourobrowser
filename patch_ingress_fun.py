import re

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'r') as f:
    content = f.read()

target = """            if scope:
                return self._create_node(MethodDefNode, name=meth_name, args=args, body=body, metadata={"type": ret_type})
            return self._create_node(FunctionDefNode, name=meth_name, args=args, body=body, metadata={"type": ret_type})"""

replacement = """            if scope:
                return self._create_node(MethodDefNode, name=meth_name, args=args, body=body, return_type=ret_type)
            return self._create_node(FunctionDefNode, name=fqdn, args=args, body=body, return_type=ret_type)"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/ingress/cpp.py', 'w') as f:
    f.write(content)
