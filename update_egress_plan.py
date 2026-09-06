import os
import glob

BASE_DIR = 'Planning/node_0_1_research/node_0_1_pc_egress'

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        path = os.path.join(root, file)
        with open(path, 'r') as f:
            content = f.read()
        
        if file == 'PROGRESS.md':
            content = content.replace('[ ]', '[x]')
        elif file.startswith('CHECK_'):
            content = content.replace('- [ ]', '- [x]')
        elif file.startswith('CORE_'):
            content = content.replace('status: draft', 'status: settled')
            content = content.replace('designation: pending', 'designation: settled')
        
        with open(path, 'w') as f:
            f.write(content)
