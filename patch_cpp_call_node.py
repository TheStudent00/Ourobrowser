import re

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'r') as f:
    content = f.read()

target = """        if isinstance(func_str, str):
            if func_str == "print":"""

replacement = """        if isinstance(func_str, str):
            mapped_fmt = self.ledger.resolve_function(func_str)
            if mapped_fmt:
                args_strs = [self.generate(arg) for arg in node.args]
                if "(" in mapped_fmt:
                    try:
                        return mapped_fmt.format(*args_strs)
                    except IndexError:
                        pass
                else:
                    func_str = mapped_fmt

            if func_str == "print":"""

content = content.replace(target, replacement)

with open('Tools/PCv3.1/pseudocoup/egress/cpp.py', 'w') as f:
    f.write(content)
