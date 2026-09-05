import re

with open('Research/chromium_compilation/ninja_error_parser.py', 'r') as f:
    content = f.read()

target = """        file_match = re.search(r"^(.*?):\d+:\d+: (?:fatal )?error:", line)
        if file_match:
            failed_files.add(file_match.group(1))"""

replacement = """        file_match = re.search(r"^(.*?):\d+:\d+: (?:fatal )?error:", line)
        if file_match:
            fpath = file_match.group(1)
            if "third_party/blink" in fpath or "v8/" in fpath:
                failed_files.add(fpath)"""

content = content.replace(target, replacement)

with open('Research/chromium_compilation/ninja_error_parser.py', 'w') as f:
    f.write(content)
