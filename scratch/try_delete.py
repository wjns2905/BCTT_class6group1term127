# -*- coding: utf-8 -*-
import os
import sys
import time
import shutil

sys.stdout.reconfigure(encoding='utf-8')

# Change working directory of THIS python process immediately
os.chdir(r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127")

bctt_path = r"C:\Users\camka\OneDrive\Desktop\BCTT"

if not os.path.exists(bctt_path):
    print("BCTT does not exist!")
    sys.exit(0)

# Check contents
files = os.listdir(bctt_path)
print(f"Files in BCTT: {files}")

# Try to remove
try:
    if os.path.isdir(bctt_path):
        # First remove any files inside
        for f in files:
            fp = os.path.join(bctt_path, f)
            if os.path.isdir(fp):
                shutil.rmtree(fp, ignore_errors=True)
            else:
                os.remove(fp)
        os.rmdir(bctt_path)
        print("SUCCESSFULLY REMOVED BCTT via Python!")
except Exception as e:
    print(f"Failed to remove BCTT: {e}")
