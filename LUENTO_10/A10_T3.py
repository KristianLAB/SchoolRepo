########################################################
# Task A10_T3
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n):
        for j in range(0, n-i-1):
            if (PAsc and PValues[j] > PValues[j+1]) or (not PAsc and PValues[j] < PValues[j+1]):
                PValues[j], PValues[j+1] = PValues[j+1], PValues[j]

def readFile(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]

def main():
    print("Program starting.")
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ")

    values = readFile(filename)
    print(f"Raw '{filename}' -> " + ", ".join(map(str, values)))

    bubbleSort(values, PAsc=True)
    print(f"Ascending '{filename}' -> " + ", ".join(map(str, values)))

    bubbleSort(values, PAsc=False)
    print(f"Descending '{filename}' -> " + ", ".join(map(str, values)))

    print("Program ending.")

if __name__ == "__main__":
    main()