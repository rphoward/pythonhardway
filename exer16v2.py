# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:28:30 2016

@author: Bob()
"""

# from sys import argv
# script, filename = argv
keyboard  = input('Enter filename?')
filename = keyboard
print('opening file :  {}   '.format(filename))
target = open(filename, "w")

print("truncating the file.  GOODBYE")
target.truncate
print("Now I'm going to ask you for three lines. ")

#line1 = input("line 1 :  ")
#line2 = input("line 2 :  ")
#line3 = input("line 3 :  ")

def intofile():
    lines = 3
    for line in range(lines):
        print(line)
        entry = input("line {} : ".format(line))
        target.write(entry) 
        target.write("\n")
intofile()

print("I'm going to write these to the file")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")


print("And finally we close it")
target.close()



