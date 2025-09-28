print("Program starting.")
print("Insert two integers.")

num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if(num1 > num2):
    print("First integer is greater.")
elif(num2 > num1):
    print("Second integer is greater.")
else:
    print("Integers are the same")


print("")

Sum = num1 + num2

print(f"{num1} + {num2} = {sum}")
print("")

Remainder = Sum % 2

if(Remainder == 0):
    print("Sum is even.")
else:
    print("Sum in odd.")
    
print("Program ending.")