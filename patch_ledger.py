import re

with open('Tools/PCv3.1/pseudocoup/core/ledger.py', 'r') as f:
    content = f.read()

# Update __init__
init_target = "        self.memory_erasure: Dict[str, str] = {}"
init_replacement = init_target + "\n        self.functions: Dict[str, str] = {}"
content = content.replace(init_target, init_replacement)

# Update dump
dump_target = "            \"memory_erasure\": self.memory_erasure"
dump_replacement = dump_target + ",\n            \"functions\": self.functions"
content = content.replace(dump_target, dump_replacement)

# Update load
load_target = "            self.memory_erasure = data.get(\"memory_erasure\", {})"
load_replacement = load_target + "\n            self.functions = data.get(\"functions\", {})"
content = content.replace(load_target, load_replacement)

# Add resolve_function
resolve_target = "        return self.types.get(fqdn)"
resolve_replacement = resolve_target + """

    def resolve_function(self, fqdn: str) -> Optional[str]:
        \"\"\"Retrieves the Python C-API function mapping for a given V8 C++ function.\"\"\"
        return self.functions.get(fqdn)"""
content = content.replace(resolve_target, resolve_replacement)

with open('Tools/PCv3.1/pseudocoup/core/ledger.py', 'w') as f:
    f.write(content)
