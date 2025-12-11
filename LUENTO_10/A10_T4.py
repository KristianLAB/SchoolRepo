########################################################
# Task A10_T4
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    PMerge.clear()
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)

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

    mergeSort(values, PAsc=True)
    print(f"Ascending '{filename}' -> " + ", ".join(map(str, values)))

    mergeSort(values, PAsc=False)
    print(f"Descending '{filename}' -> " + ", ".join(map(str, values)))

    print("Program ending.")

if __name__ == "__main__":
    main()