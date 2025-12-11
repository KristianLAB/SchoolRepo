########################################################
# Task A9_T7
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

import sys
import os

def showHelp():
    print("Usage: python {} <src_file> <dst_file>".format(sys.argv[0]))

def copyFile(src, dst):
    proceed = True
    if os.path.exists(dst):
        ans = input('Destination file "{}" exists. Overwrite? (y/n): '.format(dst))
        if ans.lower() != "y":
            proceed = False
    if proceed:
        try:
            with open(src, "r") as fsrc:
                content = fsrc.read()
            with open(dst, "w") as fdst:
                fdst.write(content)
            print('Copying file "{}" to "{}".'.format(src, dst))
        except Exception as e:
            print("Failed to copy file:", e)
            sys.exit(-1)

def main():
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid number of arguments!")
        showHelp()
        sys.exit(1)
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    if not os.path.exists(src_file):
        print('Source file "{}" does not exist.'.format(src_file))
        sys.exit(-1)
    print('Source file "{}"'.format(src_file))
    print('Destination file "{}"'.format(dst_file))
    copyFile(src_file, dst_file)
    print("Program ending.")

if __name__ == "__main__":
    main()