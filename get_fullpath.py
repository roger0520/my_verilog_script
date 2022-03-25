#!/homea01/users/tytu/anaconda3/bin/python3.7
# coding: utf-8


import os
from os.path import join
import sys

if len(sys.argv) < 2:
    print(f'\t\tformat is : get_fullpath.py root_path')
else:
    root = sys.argv[1]
    alllist = os.walk(root) #recursive search target path's file and directory
    file = [] # file list put all file name
    for root, dirs, files in alllist:
        for f in files:
            fullpath = join(root, f)
            print(fullpath)
            file.append(fullpath)
fname = sys.argv[2] # define output filename
with open(fname, 'w', encoding='utf-8') as f:
    for file_name in file:
        f.write(f'{file_name}\n')

