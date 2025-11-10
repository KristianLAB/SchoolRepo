def main():
    print("Program starting.", end="")
    choice = -1
    count = 0
    while choice != 0:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            print("Count increased!")
            count = count+1
        elif choice == 3:
            print("Cleared count!")
            count = 0
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
                   
def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return 404
        
def showOptions():
    
    print("\nOptions:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

main()

print("\nProgram ending.")