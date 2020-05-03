#!/bin/bash
# Specify the files to be backed up.
# Below command will backup everything inside the project folder

# You can also use specific files using the command git add file1 file2 ..
# Committing to the local repository with a message containing the time details

cd /Users/haneeshkesari/Downloads/PythonHK/
curtime=`date`
git add .
git commit -m "Automatic Backup @ $curtime"

# Push the local snapshot to a remote destination
git push origin master