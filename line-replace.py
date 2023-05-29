# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:46:32 2021

@author: ASUS
"""

import fileinput
import sys
import glob, os
def replacement(file, old, new):
   for line in fileinput.input(file, inplace=1):
       line = line.replace(old, new)
       sys.stdout.write(line)
       
old_line = "pseudo_dir = '/okyanus/users/salidoust/my-pseudo',"
new_line = "pseudo_dir = 'newpath',"
for infile in glob.glob("*.in"):
    replacement(infile, old_line, new_line)
