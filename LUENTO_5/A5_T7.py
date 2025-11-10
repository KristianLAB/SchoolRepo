DELIMITER = ","


def main():
    print("Program starting.")
    analyseWords(collectWords())
    


def collectWords() -> str:
    word = "i"
    words = ""
    while word != "":
        word = input("Insert word(empty stops):")
        if word != "" and words == "":
            words = words+word
        elif word != "" and words != "":
            words = words+DELIMITER+word
    return str(words)

        
def analyseWords(words: str):
    Split = words.split(sep=DELIMITER)
    print(f"- {len(Split)} Words")
    print(f"- {len(words)-len(Split)+1} Characters")
    Avg = (len(words)-len(Split)+1) / len(Split)
    print("- {:.2f} Average word length".format(Avg))
    
    
   

main()

print("Program ending.")