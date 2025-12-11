########################################################
# Task A9_T3
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

import os
import sys

print("Program starting.")

filename = input("Insert filename: ")

if not os.path.exists(filename):
    print('Error! File "{}" doesn\'t exist.'.format(filename))
    sys.exit(1)

print("## {} ##".format(filename))
with open(filename, "r") as f:
    print(f.read().strip())
print("## {} ##".format(filename))
print("Program ending.")