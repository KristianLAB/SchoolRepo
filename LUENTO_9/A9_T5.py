########################################################
# Task A9_T5
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

print("Program starting.")

try:
    r = int(input("Insert red: "))
    g = int(input("Insert green: "))
    b = int(input("Insert blue: "))
    if not all(0 <= x <= 255 for x in [r, g, b]):
        raise ValueError()
except Exception:
    print("Couldn't perform the designed task due to the invalid input values.")
else:
    print("RGB Details:")
    print("- Red {}".format(r))
    print("- Green {}".format(g))
    print("- Blue {}".format(b))
    print("- Hex #{:02x}{:02x}{:02x}".format(r, g, b))

print("Program ending.")