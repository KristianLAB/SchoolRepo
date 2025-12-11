########################################################
# Task A9_T4
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    c = input("Insert Celsius: ")
    try:
        val = float(c)
    except ValueError:
        raise ValueError("could not convert string to float: '{}'".format(c))
    if not TEMP_MIN <= val <= TEMP_MAX:
        raise Exception("{} temperature out of range.".format(val))
    return val

print("Program starting.")
try:
    celsius = collectCelsius()
    print("You inserted {} °C".format(celsius))
except Exception as e:
    print("Error:", e)
print("Program ending.")