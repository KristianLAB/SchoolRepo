########################################################
# Task A9_T1
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

print("Program starting.")

total = 0.0
while True:
    value = input("Insert a floating-point value (0 to stop): ")
    if value == "0":
        break
    try:
        fval = float(value)
        total += fval
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(value))

print("\nFinal sum is {:.2f}".format(total))
print("Program ending.")