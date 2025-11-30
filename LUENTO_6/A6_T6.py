LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cipher_text(line: str) -> str:
    result = ""
    for ch in line:
        if ch.islower():
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        elif ch.isupper():
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch
    return result



def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")

    rows = []
    while True:
        row = input("Insert row (empty stops): ")
        if row == "":
            break
        rows.append(row)

    ciphered = [cipher_text(r) for r in rows]

    print("\n#### Ciphered text ####")
    for line in ciphered:
        print(line)

    print("\n#### Ciphered text ####")
    choice = input("Insert filename to save: ")
    if choice == "":
        print("File name not defined.")
        print("Aborting save opertation.")

    if choice.strip() != "":
        with open(choice, "w", encoding="utf-8") as f:
            for line in ciphered:
                f.write(line + "\n")
        print("Ciphered text saved!")

    print("Program ending.")
    

if __name__ == "__main__":
    main()
