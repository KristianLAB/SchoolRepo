#1. Print “Calculate the area of a wall.”
print("Calculate the area of a wall")
#2. Prompt user
    #.  1 "Enter the width in meters: ”
    #.  2 Store the input value into Feed variable.
Feed = input("Enter the width in meters: ")
    

#3. Convert the Feed variable into an integer and store it in Width variable
Width = int(Feed)
#4. Prompt user
    #.  1 “Enter the height in meters: ”  
    #.  2 store the input value into Feed variable.
Feed = input("Enter the height in meters: ")      
#5. Convert the Feed variable into an integer and store it in Height variable
Height = int(Feed)

#6. Print “Width is {Width} m and height is {Height} m.”
print(f"Width is {Width} m and height is {Height} m.")
#7. Multiply Width and Height, then store the result in Area variable
Area= Width * Height
#8. Display results to the user: “The wall will be {Area} square meters.”
print(f"The wall will be {Area} square meters.")
# Try the program with different inputs e.g. decimals. Notice any problems in the program? Are you able to solve the issue?