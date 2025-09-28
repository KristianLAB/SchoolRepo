print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

Choice = int(input("Your choice: "))

if(Choice == 1):
    print("Length options: ")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))
    if(Choice2 == 1):
        Meters = float(input("Insert meters: "))
        print(f"{Meters} m is {Meters / 1000} km")
    elif(Choice2 == 2):
        km = float(input("Insert kilometers: "))
        print(f"{km} km is {km * 1000} m")
    elif(Choice2 == 0):
        print("Exiting...")
    else:
        print("Unkown option.")
        
    
elif(Choice == 2):
    print("Weight options: ")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice2 = int(input("Your choice: "))
    if(Choice2 == 1):
        Grams = float(input("Insert grams: "))
        print(f"{Grams} g is {round(Grams * 0.00220462262 ,1)} lb")
    elif(Choice2 == 2):
        lb = float(input("Insert pounds: "))
        print(f"{lb} lb is {round(lb / 0.00220462262 ,1)} g")
    elif(Choice2 == 0):
        print("Exiting...")
    else:
        print("Unkown option.")
    
    
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")   
    
print("Program ending.")
