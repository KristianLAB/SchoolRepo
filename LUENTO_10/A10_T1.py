########################################################
# Task A10_T1
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

print("Program starting.")

filename = input("Insert filename: ")

try:
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Error! File '{}' not found.".format(filename))
    exit(1)

print("# --- Vertically --- #")
for line in lines:
    print(line)
print("# --- Vertically --- #")

print("# --- Horizontally --- #")
print(", ".join(lines))
print("# --- Horizontally --- #")

print("Program ending.")