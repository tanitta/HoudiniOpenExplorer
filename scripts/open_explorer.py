import subprocess
import sys
import os
import hou

def open_explorer(path):
    fixed_path = path.replace('/', '\\')
    print(fixed_path)
    subprocess.Popen('explorer ' + fixed_path)

raw_path = (sys.argv[1])
if raw_path[0] == '$':
    raw_path = hou.getenv(raw_path[1:])
dirname = raw_path
if not os.path.isdir(raw_path):
    dirname = os.path.dirname(raw_path) 
dirname = os.path.normpath(dirname)
open_explorer(dirname)
