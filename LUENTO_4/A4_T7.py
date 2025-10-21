print("Program starting.\n")

print("Check multiplicative persistence.")

Value = int(input("Insert an integer: "))
steps = 0

while Value >= 10:
    alkukerroin = 1
    lukujenmaara = str(Value)
    looppi_indexi = 0

    for i in str(Value):
        alkukerroin = alkukerroin * int(i)
        if looppi_indexi < len(lukujenmaara) - 1:
            print(i, end= " * ")
        else:
            print(i, end= " ")
        looppi_indexi = looppi_indexi + 1

    Value = alkukerroin
    print (f"= {Value}")
    steps = steps + 1

print("No more steps.")
print(f"\nThis program took {steps} step(s)")
print("\nProgram ending.")