import time

def Options():
    print("Options: ")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def getNumericInput(prompt, value_type=float):
    while True:
        try:
            value = value_type(input(prompt))
            return value
        
        except ValueError:
            print(f"Invalid input. Please enter a valid {value_type.__name__}.")

        except (KeyboardInterrupt, EOFError):
            print("\nUser interrupted. Returning to menu.")
            return None

def main():
    print("Program starting.")
    
    pause = None
    
    while True:
        Options()

        choice = input("Your choice: ").strip()

        if choice == "1":
            result = getNumericInput("Insert pause duration (s): ", float)

            if result is not None:
                pause = result
                print(f"Pause duration set to {pause} seconds.\n")

        elif choice == "2":
            if pause is None:
                print("Error: Pause duration not set. Please set it first (option 1).\n")

            else:
                print(f"Pausing for {pause} seconds.")
                time.sleep(pause)
                print("Unpaused.\n")

        elif choice == "0":
            print("Exiting...")
            print("Program ending.")
            break

        else:
            print("Invalid choice. Please try asgain. \n")

if __name__ == "__main__":
    main() 