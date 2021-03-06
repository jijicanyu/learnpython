#!/usr/bin/python
# Filename: backup_ver2.py

import os
import time

# 1. The files and directions to be backed up are specified in a list
source = 'G:\\learnpython\\readme.md'
# 2. The backup must be stored in a main backup directory
target_dir = 'G:'
# 3. The files are backed up into a rar file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the rar archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today
# The name of the rar file
target = today + os.sep + now + '.rar'

rar_command = "WinRAR a %s %s -r" % (target, source)
# Run the backup
if os.system(rar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
