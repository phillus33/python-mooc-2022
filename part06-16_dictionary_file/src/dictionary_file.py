def add_word(fin: str, eng: str):
    with open("dictionary.txt", "a") as dic_file:
        dic_file.write(f"{fin} - {eng}\n")

def return_word(search_term: str):
    with open("dictionary.txt") as dic_file:
        for line in dic_file:
            line = line.replace("\n", "")
            if search_term in line:
                print(line)

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    command = input("Function: ")

    if command == "1":
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        add_word(finnish_word, english_word)
        print("Dictionary entry added")
    
    elif command == "2":
        word = input("Search term: ")
        return_word(word)
    
    elif command == "3":
        print("Bye!")
        break