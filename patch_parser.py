import re

with open('Research/chromium_compilation/ninja_error_parser.py', 'r') as f:
    content = f.read()

# Make sure it only extracts files from third_party/blink or v8/
target = """            if file_path:
                failed_files.add(file_path)"""

replacement = """            if file_path:
                if "third_party/blink" in file_path or "v8/" in file_path:
                    failed_files.add(file_path)"""

content = content.replace(target, replacement)

with open('Research/chromium_compilation/ninja_error_parser.py', 'w') as f:
    f.write(content)
