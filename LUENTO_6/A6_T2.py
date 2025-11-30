def writeFile(PFileName, PContent) -> None:
    Filehandle = open(PFileName, "w")
    Filehandle.write(PContent)
    Filehandle.close()
    return None

def main() -> None:
    print("Program starting.")
    firstName = input("Insert first name: ")
    lastName = input("Insert last name: ")
    fileName = input("Insert file name: ")
    Content = "{}\n{}".format(firstName, lastName)
    writeFile(fileName, Content)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()