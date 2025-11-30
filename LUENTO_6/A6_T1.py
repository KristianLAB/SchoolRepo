def readFile(Filename):
    Filehandler = open(Filename, "r")
    Content = ""
    Row = Filehandler.readline()
    while Row != "":
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content # Palaa takaisin kutsukohtaan


def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename) # Hyppää readFile funktioon
    print("#### START {} ####".format(Filename))
    print(FileContent)
    print("#### END {} ####".format(Filename))
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
    