# -*- coding: utf-8 -*-
import subprocess
import sys

# Spawn a completely detached process with cwd = BCTT_class6group1term127
cmd = [
    sys.executable,
    "-c",
    """
import os, time, sys, shutil
time.sleep(3)
target = r'C:\\Users\\camka\\OneDrive\\Desktop\\BCTT'
for attempt in range(10):
    if not os.path.exists(target):
        print('Already gone!')
        break
    try:
        shutil.rmtree(target, ignore_errors=False)
        print('Successfully deleted BCTT on attempt', attempt)
        break
    except Exception as e:
        print(f'Attempt {attempt} failed: {e}')
        time.sleep(1)
"""
]

subprocess.Popen(
    cmd,
    cwd=r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127",
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS if sys.platform == 'win32' else 0,
    close_fds=True
)

print("Detached delete worker launched successfully with CWD BCTT_class6group1term127!")
