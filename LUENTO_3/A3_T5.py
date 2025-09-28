print("Program starting.")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

Choice = int(input("Your choice: "))


if(Choice == 1):
    Celc = int(input("Insert the amount of Celsius: "))
    Fah = (Celc *1.8) + 32
    print(f"{Celc}°C equals to {Fah}°F")
elif(Choice == 2):
    Fah = int(input("Insert the amount of Fahrenheit: "))
    Celc = (Fah - 32) / 1.8
    print(f"{Fah}°F equals to {round(Celc,1)}°C")
elif(Choice == 0):
    print("Exiting...")
   
print("Program ending.") 





