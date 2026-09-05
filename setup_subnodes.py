import os
import shutil

BASE_DIR = 'Planning/node_0_1_research/node_0_7_api_mapping'

subnodes = [
    {
        "id": "ourobrowser.root.research.api_mapping.ledger_extension",
        "name": "ledger_extension",
        "dir": "node_0_0_ledger_extension",
        "core": "CORE_0_0_ledger_extension.md",
        "designation": "code (module)",
        "definition": "Extend the PCv3.1 Ledger in `pseudocoup/core/ledger.py` to ingest a `\"functions\"` block and provide a `resolve_function(fqdn)` method."
    },
    {
        "id": "ourobrowser.root.research.api_mapping.call_node_interceptor",
        "name": "call_node_interceptor",
        "dir": "node_0_1_call_node_interceptor",
        "core": "CORE_0_1_call_node_interceptor.md",
        "designation": "code (module)",
        "definition": "Modify `CppEmitter.visit_CallNode` in `pseudocoup/egress/cpp.py` to flatten `node.func_name` to an FQDN, resolve it via the Ledger, and restructure arguments using format strings."
    },
    {
        "id": "ourobrowser.root.research.api_mapping.trickle_injection",
        "name": "trickle_injection",
        "dir": "node_0_2_trickle_injection",
        "core": "CORE_0_2_trickle_injection.md",
        "designation": "code (module)",
        "definition": "Update `transpiler_loop.py` to inject the `GLOBAL_FUNCTIONS` dict containing known V8 to CPython mappings directly into the generated `.ledger.json`."
    }
]

# Update parent CORE file
parent_core_path = os.path.join(BASE_DIR, 'CORE_0_7_api_mapping.md')
with open(parent_core_path, 'r') as f:
    parent_core = f.read()

subnodes_yaml = ""
subnodes_md = ""

for sn in subnodes:
    subnodes_yaml += f"    - name: {sn['name']}\n      path: {sn['dir']}/{sn['core']}\n"
    subnodes_md += f"- [{sn['name']}]({sn['dir']}/{sn['core']}) — {sn['definition']}\n"

parent_core = parent_core.replace("sub_nodes: []", "sub_nodes:\n" + subnodes_yaml.rstrip())
parent_core = parent_core.replace("*(none)*", subnodes_md.strip())

with open(parent_core_path, 'w') as f:
    f.write(parent_core)

# Create subnode directories and files
for sn in subnodes:
    sn_dir = os.path.join(BASE_DIR, sn['dir'])
    os.makedirs(sn_dir, exist_ok=True)
    
    core_content = f"""---
id: {sn['id']}
level: 3
status: draft
settled_by: Dee
supersedes: null
designation: {sn['designation']}
node:
    name: {sn['name']}
    path: {sn_dir}/{sn['core']}
super_node:
    name: api_mapping
    path: ../CORE_0_7_api_mapping.md
sub_nodes: []
---

# CORE 0_7_{sn['dir'].split('_')[2]} — {sn['name']}

## metadata

- **id:** {sn['id']}
- **level:** 3
- **status:** draft
- **designation:** {sn['designation']}
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [api_mapping](../CORE_0_7_api_mapping.md)

## sub_nodes

*(none)*

## definition

{sn['definition']}
"""
    with open(os.path.join(sn_dir, sn['core']), 'w') as f:
        f.write(core_content)
        
    check_content = f"""# CHECK 0_7_{sn['dir'].split('_')[2]} — {sn['name']}

- [ ] Does {sn['name']} successfully pass verification?
"""
    with open(os.path.join(sn_dir, f"CHECK_0_{sn['dir'].split('_')[2]}_{sn['name']}.md"), 'w') as f:
        f.write(check_content)

    prog_content = f"""# PROGRESS 0_7_{sn['dir'].split('_')[2]} — {sn['name']}

- [ ] **planned** — Implement {sn['name']}.
"""
    with open(os.path.join(sn_dir, 'PROGRESS.md'), 'w') as f:
        f.write(prog_content)

print("Subnodes created.")
