# -*- coding: utf-8 -*-
import subprocess, os, sys
sys.stdout.reconfigure(encoding='utf-8')

test_file = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\scratch\test_node_runtime.js"
res = subprocess.run(["node", test_file], capture_output=True, text=True, encoding='utf-8')
print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)
print("Returncode:", res.returncode)
