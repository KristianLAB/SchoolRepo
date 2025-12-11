########################################################
# Task A10_T2
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

import sys
from functools import reduce
import operator

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as f:
            for line in f:
                s = line.strip()
                if s:
                    PValues.append(int(s))
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    return reduce(operator.mul, PValues, 1)

def main() -> None:
    Values: list[int] = []

    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)

    print("# --- Sum of numbers --- #")
    print(sumOfValues(Values))
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(productOfValues(Values))
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()