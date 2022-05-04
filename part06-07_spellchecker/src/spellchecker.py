dictionary = {}
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()

        if line[0] not in dictionary:
            dictionary[line[0]] = [line]
        else:
            dictionary[line[0]].append(line)


text = input("Write text: ")


for word in text.split(" "):
    if word.lower() not in dictionary[word[0].lower()]:
        print(f"*{word}*", end=" ")
    else:
        print(word, end=" ")


