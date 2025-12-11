def int_collector():
    numbers: list[int] = []  
    
    while True:
        try:
            Feed = int(input("Insert positive integer (negative stops): "))
        
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if Feed < 0:
            break
        elif Feed > 0:
            numbers.append(Feed)
        else:
            print("Zero is not collected. Please enter a positive integer or a negative integer to stop.")
            
        print("Stopped collecting positive integers: ")
        
        if numbers:
            print(f"Displaying {len(numbers)} integers: ")
            for index, value in enumerate(numbers):
                
                ordinal = index +1
                print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")
        
        else:
            print("No integers to display.")

def main():
    print("Program starting.")
    print("Collect positive integers.")
    int_collector()
    print("Program ending.")

    

if __name__ == "__main__":
    main()