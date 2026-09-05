import os
import yaml

def parse_frontmatter(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                return yaml.safe_load(content[3:end])
    except Exception:
        pass
    return {}

def print_tree(start_path, indent=""):
    items = sorted(os.listdir(start_path))
    core_files = [i for i in items if i.startswith("CORE_") and i.endswith(".md")]
    
    if not core_files:
        return
        
    core_file = core_files[0]
    fm = parse_frontmatter(os.path.join(start_path, core_file))
    
    node_name = fm.get('node', {}).get('name', os.path.basename(start_path))
    designation = fm.get('designation', 'unknown')
    status = fm.get('status', 'unknown')
    
    print(f"{indent}- **{node_name}** [{designation}] ({status})")
    
    for item in items:
        full_path = os.path.join(start_path, item)
        if os.path.isdir(full_path) and item.startswith("node_"):
            print_tree(full_path, indent + "  ")

print_tree("Planning/")
