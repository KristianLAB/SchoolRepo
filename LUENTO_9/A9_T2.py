########################################################
# Task A9_T2
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

import sys

print("Program starting.")

code = input("Insert exit code(0-255): ")
try:
    code_int = int(code)
    if not 0 <= code_int <= 255:
        raise ValueError("Exit code out of range")
except ValueError:
    print("Invalid exit code, using 1 instead.")
    code_int = 1

print("Clean exit")
sys.exit(code_int)