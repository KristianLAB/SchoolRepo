print("Program starting.")

print("Estimate how many minutes you spent on programming...\n")

A1_T1 = int(input("A1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))

Total = A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7
Average = float(Total / 7)

print(f"\nIn total you spent {Total} minutes on programming.")

print(f"Average per task was {round(Average,2)} min and same rounded to the nearest integer {round(Average)} min.")

print("\nProgram ending.")
