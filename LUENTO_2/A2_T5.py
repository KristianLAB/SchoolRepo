print("Program starting.\n")

word = input("Insert a closed compound word: ")

print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")

print(f"The inserted word length is {len(word)}")

print(f"Last character is '{word[-1]}'")



print(f"Take substring from the inserted word by inserting...")

starting_point = int(input("1) Starting point: "))
ending_point = int(input("2) Ending point: "))
step_size = int(input("3) Step size: "))

substring = word[starting_point:ending_point:step_size]

print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")

print("Program ending.")