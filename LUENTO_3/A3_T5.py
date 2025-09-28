print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

Choice = int(input("Your choice: "))


if(Choice == 1):
    Celc = float(input("Insert the amount of Celsius: "))
    Fah = (Celc *1.8) + 32
    print(f"{Celc} °C equals to {round(Fah,1)} °F")
elif(Choice == 2):
    Fah = float(input("Insert the amount of Fahrenheit: "))
    Celc = (Fah - 32) / 1.8
    print(f"{Fah} °F equals to {round(Celc,1)} °C")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")
   
print("\nProgram ending.") 





