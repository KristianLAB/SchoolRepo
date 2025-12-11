########################################################
# Task A9_T6
# Developer Kristian Olkkola
# Date 2025-12-10
########################################################

lines = []

def menu():
    print("\nOptions:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")
    return input("Your choice: ")

def save_lines():
    if not lines:
        print("No lines to save.")
        return
    filename = input("Insert filename: ")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print("Lines saved to {}".format(filename))

print("Program starting.")

try:
    while True:
        choice = menu()
        if choice == "1":
            line = input("Insert text: ")
            lines.append(line)
        elif choice == "2":
            save_lines()
        elif choice == "0":
            break
except KeyboardInterrupt:
    print("\nKeyboard interrupt and unsaved progress!")
    if lines:
        save = input("Save before quit(y/n)?: ")
        if save.lower() == "y":
            save_lines()
print("Program ending.")