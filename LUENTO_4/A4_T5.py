print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
Run = True

if start >= stop:
    print("\nStarting point value must be less than the stopping point value.", end="")
    Run = False

if (inspection < start) or (inspection > stop):
     print("\nInspection value must be within the range of start and stop.", end="")
     Run = False
 
if Run is True:
   print("\nFirst loop - inspection with break:")
   for nro in range(start, stop):
       if nro == inspection:
           break
       else:
           print(nro, end= " ")
           
   print("\nSecond loop - inspection with continue:")
   for nro in range(start, stop):
       if nro == inspection:
           continue
       else:
           print(nro, end= " ")

print("\n\nProgram ending.")