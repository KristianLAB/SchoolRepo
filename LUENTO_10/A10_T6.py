########################################################
# Task A10_T6
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

import time
import copy

def bubbleSort(PNums: list[int]) -> list[int]:
    n = len(PNums)
    arr = PNums[:]
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quickSort(PNums: list[int]) -> list[int]:
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[0]
    left = [x for x in PNums[1:] if x <= pivot]
    right = [x for x in PNums[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def measureSortingTime(PSortingAlgorithm, PArr):
    start = time.perf_counter_ns()
    PSortingAlgorithm(copy.deepcopy(PArr))
    end = time.perf_counter_ns()
    return end - start

def readValues(PValues: list[int]) -> None:
    PValues.clear()
    filename = input("Insert dataset filename: ")
    with open(filename, "r") as f:
        for line in f:
            s = line.strip()
            if s:
                PValues.append(int(s))

def main():
    Values: list[int] = []
    Results: list[str] = []

    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            readValues(Values)
        elif choice == "2":
            builtinTime = measureSortingTime(sorted, Values)
            bubbleTime = measureSortingTime(bubbleSort, Values)
            quickTime = measureSortingTime(quickSort, Values)
            print(f"Measured speeds for dataset:")
            print(f" - Built-in sorted {builtinTime} ns")
            print(f" - Buble sort {bubbleTime} ns")
            print(f" - Quick sort {quickTime} ns")
            Results = [
                f"Built-in sorted {builtinTime} ns",
                f"Buble sort {bubbleTime} ns",
                f"Quick sort {quickTime} ns"
            ]
        elif choice == "3":
            filename = input("Insert results filename: ")
            with open(filename, "w") as f:
                for line in Results:
                    f.write(line + "\n")
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()