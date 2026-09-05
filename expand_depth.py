import os
import glob

BASE_DIR = 'Planning/node_0_1_research/node_0_7_api_mapping'

layers = {
    "node_0_0_ledger_extension": [
        {
            "id": "ourobrowser.root.research.api_mapping.ledger_extension.schema_update",
            "name": "schema_update",
            "dir": "node_0_0_schema_update",
            "designation": "code (patch)",
            "definition": "Update the Ledger initialization to accept the 'functions' mapping schema block."
        },
        {
            "id": "ourobrowser.root.research.api_mapping.ledger_extension.resolve_method",
            "name": "resolve_method",
            "dir": "node_0_1_resolve_method",
            "designation": "code (module)",
            "definition": "Implement the `resolve_function(fqdn)` logic to query the function mapping dictionary."
        }
    ],
    "node_0_1_call_node_interceptor": [
        {
            "id": "ourobrowser.root.research.api_mapping.call_node_interceptor.fqdn_resolver",
            "name": "fqdn_resolver",
            "dir": "node_0_0_fqdn_resolver",
            "designation": "code (module)",
            "definition": "Flatten complex `AttributeNode` and `IdentifierNode` combinations into a single FQDN string before querying."
        },
        {
            "id": "ourobrowser.root.research.api_mapping.call_node_interceptor.format_evaluator",
            "name": "format_evaluator",
            "dir": "node_0_1_format_evaluator",
            "designation": "code (module)",
            "definition": "Evaluate parameter string formatting so the transpiler can drop or rearrange arguments (e.g. mapping `{1}` to drop `{0}`)."
        }
    ],
    "node_0_2_trickle_injection": [
        {
            "id": "ourobrowser.root.research.api_mapping.trickle_injection.mapping_dictionary",
            "name": "mapping_dictionary",
            "dir": "node_0_0_mapping_dictionary",
            "designation": "code (config)",
            "definition": "Create the `GLOBAL_FUNCTIONS` constant dictionary holding all known V8 to CPython C-API mappings."
        },
        {
            "id": "ourobrowser.root.research.api_mapping.trickle_injection.ledger_writer",
            "name": "ledger_writer",
            "dir": "node_0_1_ledger_writer",
            "designation": "code (patch)",
            "definition": "Patch `transpiler_loop.py` to seamlessly bake the `GLOBAL_FUNCTIONS` into the dynamically generated `.ledger.json`."
        }
    ]
}

for parent_dir, subnodes in layers.items():
    parent_core_path = glob.glob(os.path.join(BASE_DIR, parent_dir, "CORE_*.md"))[0]
    
    with open(parent_core_path, 'r') as f:
        parent_core = f.read()

    subnodes_yaml = ""
    subnodes_md = ""

    for sn in subnodes:
        subnodes_yaml += f"    - name: {sn['name']}\n      path: {sn['dir']}/CORE_0_{sn['dir'].split('_')[2]}_{sn['name']}.md\n"
        subnodes_md += f"- [{sn['name']}]({sn['dir']}/CORE_0_{sn['dir'].split('_')[2]}_{sn['name']}.md) — {sn['definition']}\n"

    parent_core = parent_core.replace("sub_nodes: []", "sub_nodes:\n" + subnodes_yaml.rstrip())
    parent_core = parent_core.replace("*(none)*", subnodes_md.strip())

    with open(parent_core_path, 'w') as f:
        f.write(parent_core)

    for sn in subnodes:
        sn_dir = os.path.join(BASE_DIR, parent_dir, sn['dir'])
        os.makedirs(sn_dir, exist_ok=True)
        
        core_name = f"CORE_0_{sn['dir'].split('_')[2]}_{sn['name']}.md"
        
        core_content = f"""---
id: {sn['id']}
level: 4
status: draft
settled_by: Dee
supersedes: null
designation: {sn['designation']}
node:
    name: {sn['name']}
    path: {sn_dir}/{core_name}
super_node:
    name: {parent_dir.split('_', 3)[3]}
    path: ../{os.path.basename(parent_core_path)}
sub_nodes: []
---

# CORE 0_{sn['dir'].split('_')[2]} — {sn['name']}

## metadata

- **id:** {sn['id']}
- **level:** 4
- **status:** draft
- **designation:** {sn['designation']}
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [{parent_dir.split('_', 3)[3]}](../{os.path.basename(parent_core_path)})

## sub_nodes

*(none)*

## definition

{sn['definition']}
"""
        with open(os.path.join(sn_dir, core_name), 'w') as f:
            f.write(core_content)
            
        check_content = f"""# CHECK 0_{sn['dir'].split('_')[2]} — {sn['name']}

- [ ] Does {sn['name']} successfully pass verification?
"""
        with open(os.path.join(sn_dir, f"CHECK_0_{sn['dir'].split('_')[2]}_{sn['name']}.md"), 'w') as f:
            f.write(check_content)

        prog_content = f"""# PROGRESS 0_{sn['dir'].split('_')[2]} — {sn['name']}

- [ ] **planned** — Implement {sn['name']}.
"""
        with open(os.path.join(sn_dir, 'PROGRESS.md'), 'w') as f:
            f.write(prog_content)

print("Layer expanded.")
