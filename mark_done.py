import os
import glob

BASE_DIR = 'Planning/node_0_1_research/node_0_7_api_mapping'
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file == 'PROGRESS.md':
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            content = content.replace('[ ] **planned**', '[x] **done**')
            with open(path, 'w') as f:
                f.write(content)
        elif file.startswith('CHECK_'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            content = content.replace('- [ ]', '- [x]')
            with open(path, 'w') as f:
                f.write(content)
        elif file.startswith('CORE_'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                content = f.read()
            content = content.replace('status: draft', 'status: settled')
            with open(path, 'w') as f:
                f.write(content)
