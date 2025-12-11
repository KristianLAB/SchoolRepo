def integers():
    feed = input("Insert comma separated integers: ")
    numbers = feed.split(",")
    valid_num: list[int] = []

    for number in numbers:
        number = number.strip()

        try:
            num = int(number)
            valid_num.append(num)

        except ValueError:
            print(f"Invalid value '{number}' detected.")

    if not valid_num:
        print("No valid integers to analyze.")
        return
    
    Sum = sum(valid_num)
    count = len(valid_num)
    parity = "even" if Sum % 2 == 0 else "odd"

    print(f"There are {count} integers in the list.")
    print(f"Sum of the integers is {Sum} and it's {parity}")

def main():
    print("Program starting.")
    integers()
    print("Program ending.")

if __name__ == "__main__":
    main()