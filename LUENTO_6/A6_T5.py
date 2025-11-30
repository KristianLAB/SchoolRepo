SEPARATOR = ";"

def read_values(filename: str) -> str:
    values = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            clean = line.strip()
            if clean:
                values += clean + SEPARATOR
    return values


def analyse_numbers(values_str: str) -> tuple[int, int, int, float]:
    numbers = [int(v) for v in values_str.split(SEPARATOR) if v]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    return count, total, greatest, average


def main():
    print("Program starting.")
    
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    
    values_str = read_values(filename)
    
    print(f'File "{filename}" results:')

    count, total, greatest, average = analyse_numbers(values_str)

    print("Count;Sum;Greatest;Average")
    print(f"{count};{total};{greatest};{average:.2f}")

    print("\n#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()
