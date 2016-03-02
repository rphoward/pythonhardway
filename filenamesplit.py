# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:18:22 2016

@author: Bob
"""


from sys import argv
import ntpath
print(argv)
path = argv
print(path)
filename = ntpath.basename(path)
print(filename)

