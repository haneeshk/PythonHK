#!/usr/bin/env python3
import time
import os;
import subprocess



while True:

    os.chdir("/Users/haneeshkesari/Downloads/PythonHK")
    result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
    # print(result.stdout)
    # print("Pushing PythonHK repo to remote origin")
    os.system('git add .')
    os.system('git commit -m "Python Pushing" ')
    os.system('git push origin master')
    time.sleep(300)

    os.chdir("/Users/haneeshkesari/Downloads/appliedmechanicslab")
    result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
    print(result.stdout)
    print("Pushing appliedmechanicslab repo to remote origin")
    os.system('git add .')
    os.system('git commit -m "Python Pushing" ')
    os.system('git push origin master')
    time.sleep(300)
