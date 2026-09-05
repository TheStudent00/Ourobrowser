import re

with open('Planning/node_0_1_research/CORE_0_1_research.md', 'r') as f:
    content = f.read()

# Add to frontmatter
frontmatter_target = "    - name: incremental_compilation\n      path: node_0_6_incremental_compilation/CORE_0_6_incremental_compilation.md\n"
frontmatter_replacement = frontmatter_target + "    - name: api_mapping\n      path: node_0_7_api_mapping/CORE_0_7_api_mapping.md\n"
content = content.replace(frontmatter_target, frontmatter_replacement)

# Add to sub_nodes list
list_target = "- [incremental_compilation](node_0_6_incremental_compilation/CORE_0_6_incremental_compilation.md)"
list_replacement = list_target + "\n- [api_mapping](node_0_7_api_mapping/CORE_0_7_api_mapping.md) — Extend PCv3.1 to map V8 API function calls to CPython C-API functions."
content = content.replace(list_target, list_replacement)

with open('Planning/node_0_1_research/CORE_0_1_research.md', 'w') as f:
    f.write(content)

