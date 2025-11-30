def main() -> None:
    print("Program starting")
    print("This program analyses a list of names from a file.")
    

    filename = input("Insert filename to read: ")
    print(f"Reading names from \"{filename}\".")
    with open (filename, "r", encoding="UTF-8") as file:
        Nimet = file.read()
        for line in Nimet:
            clean = line.strip()
        if clean:
            names.append(clean)
            
    print("Analysing names...")
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    
    x = Nimet.split()
    names = (len(x))
    print(f"Name count: {names}")
    shortest = (min(x, key=len))
    longest= (max(x, key=len))
    average = sum(map(len, x))/float(len(x))
    print(f"Shortest name - {len (shortest)}")
    print(f"Longest name - {len (longest)}")
    print(f"Average name - {average:.2f} chars")
    
    
    
if __name__ == "__main__":
    main()