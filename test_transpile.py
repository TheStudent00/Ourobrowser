import sys
import os
import subprocess

abs_path = "/tmp/bigint.cc"

with open(abs_path, 'r') as f:
    content = f.read()

content = content.replace('namespace blink {', '// namespace blink {')
content = content.replace('}  // namespace blink', '// }  // namespace blink')

with open(abs_path, 'w') as f:
    f.write(content)

env = os.environ.copy()
env["PYTHONPATH"] = "/home/lucas/Programming/Ourobrowser/Tools/PCv3.1"
subprocess.run([sys.executable, "/home/lucas/Programming/Ourobrowser/Tools/PCv3.1/pseudocoup/cli.py", "--source", abs_path, "--source-lang", "cpp", "--target-lang", "cpp"], check=True, env=env)
