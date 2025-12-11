########################################################
# Task A10_T7
# Developer Kristian Olkkola
# Date 2025-12-11
########################################################

import random
random.seed(1234)

def layMines(PMineField, PMines):
    rows = len(PMineField)
    cols = len(PMineField[0])
    all_positions = [(r, c) for r in range(rows) for c in range(cols)]
    mine_positions = random.sample(all_positions, PMines)
    for r, c in mine_positions:
        PMineField[r][c] = 9

def calculateNearbys(PMineField):
    rows = len(PMineField)
    cols = len(PMineField[0])
    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if PMineField[nr][nc] == 9:
                            count +=1
            PMineField[r][c] = count

def generateMinefield(PMineField, PRows, PCols, PMines):
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0]*PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def main():
    minefield = []

    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            rows = int(input("Insert rows: "))
            cols = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(minefield, rows, cols, mines)
        elif choice == "2":
            for row in minefield:
                print(row)
        elif choice == "3":
            filename = input("Insert filename: ")
            with open(filename, "w") as f:
                for row in minefield:
                    f.write(",".join(map(str,row)) + "\n")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")
    print("Program ending.")

if __name__ == "__main__":
    main()