#!/usr/bin/env python3
import time
import os;
import subprocess


os.chdir("/Users/haneeshkesari/Downloads/PythonHK")
result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
print(result.stdout)
while True:
    time.sleep(600)
    print("Pusing file to remote repo")
    os.system('git add .')
    # os.system('git add .')
    os.system('git commit -m "Python Pushing" ')
    os.system('git push origin master')
