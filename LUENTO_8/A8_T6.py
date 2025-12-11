import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))
    print("Square added!\n")
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X: "))
    cy = int(input("- Center Y: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke))
    print("Circle added!\n")
    return None

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    confirm = input("Proceed (y/n)?: ").strip().lower()
    if confirm == "y":
        PDwg.save(pretty=True, indent=2, filename=filename)
        print("Vector saved successfully!\n")
    else:
        print("Save cancelled.\n")
    return None

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()

    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            drawSquare(Dwg)
        elif choice == "2":
            drawCircle(Dwg)
        elif choice == "3":
            saveSvg(Dwg)
        elif choice == "0":
            print("Exiting program.\nProgram ending.")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()