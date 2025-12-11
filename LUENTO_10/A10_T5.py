########################################################
# Task A10_T5
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

print("Program starting.")
n = int(input("Insert factorial: "))
result = recursiveFactorial(n)
print(f"Factorial {n}!\n{n} = {result}")
print("Program ending.")