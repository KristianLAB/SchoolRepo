import svgwrite
import math

shapes = []

def draw_square():
    x = int(input("Insert top-left X: "))
    y = int(input("Insert top-left Y: "))
    size = int(input("Insert side length: "))
    fill = input("Insert fill color: ")
    stroke = input("Insert stroke color: ")
    
    square = svgwrite.shapes.Rect(insert=(x, y), size=(size, size),
                                  fill=fill, stroke=stroke)
    shapes.append(square)
    print("Square added!")


def draw_circle():
    cx = int(input("Insert center X: "))
    cy = int(input("Insert center Y: "))
    r = int(input("Insert radius: "))
    fill = input("Insert fill color: ")
    stroke = input("Insert stroke color: ")
    
    circle = svgwrite.shapes.Circle(center=(cx, cy), r=r,
                                    fill=fill, stroke=stroke)
    shapes.append(circle)
    print("Circle added!")


def draw_hexagon():
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    circumradius = apothem / math.cos(math.radians(30))


    points = []
    for i in range(6):
        angle_deg = 30 + i * 60
        angle_rad = math.radians(angle_deg)
        x = round(cx + circumradius * math.cos(angle_rad))
        y = round(cy - circumradius * math.sin(angle_rad))
        points.append((x, y))
    
    hexagon = svgwrite.shapes.Polygon(points=points, fill=fill, stroke=stroke)
    shapes.append(hexagon)
    print("Hexagon added!")


def save_svg():
    filename = input("Insert filename: ")
    confirm = input(f'Saving file to "{filename}"\nProceed (y/n)?: ')
    if confirm.lower() == "y":
        dwg = svgwrite.Drawing(filename, profile='tiny')
        for shape in shapes:
            dwg.add(shape)
        dwg.save()
        print("Vector saved successfully!")


def main():
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            draw_square()
        elif choice == "2":
            draw_circle()
        elif choice == "3":
            draw_hexagon()
        elif choice == "4":
            save_svg()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")
    print("Program ending.")


if __name__ == "__main__":
    main()
