#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

def parse_ninja_log(filepath):
    print(f"Parsing {filepath}...")
    
    missing_includes = defaultdict(int)
    undefined_symbols = defaultdict(int)
    failed_files = set()
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        # Match "fatal error: 'v8.h' file not found"
        include_match = re.search(r"fatal error: '(.*?)' file not found", line)
        if include_match:
            missing_includes[include_match.group(1)] += 1
            
        # Match "undefined reference to `v8::Isolate::GetCurrent()'"
        undef_match = re.search(r"undefined reference to `(.*?)'", line)
        if undef_match:
            undefined_symbols[undef_match.group(1)] += 1
            
        # Extract the file that actually threw the error
        file_match = re.search(r"^(.*?):\d+:\d+: fatal error:", line)
        if file_match:
            failed_files.add(file_match.group(1))

    print("\n--- Failed Source Files ---")
    for file in sorted(failed_files):
        print(file)
            
    print("\n--- Missing Includes ---")
    for inc, count in sorted(missing_includes.items(), key=lambda x: x[1], reverse=True):
        print(f"[{count}x] {inc}")
        
    print("\n--- Undefined Symbols ---")
    for sym, count in sorted(undefined_symbols.items(), key=lambda x: x[1], reverse=True):
        print(f"[{count}x] {sym}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ninja_error_parser.py <ninja_output.log>")
        sys.exit(1)
    parse_ninja_log(sys.argv[1])
