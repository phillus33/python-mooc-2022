from difflib import get_close_matches

def main():
    with open("wordlist.txt") as words:
        word_list = []
        for line in words:
            line = line.replace("\n", "")
            word_list.append(line)
            
    sentence = input("write text: ")
    # sentence = "We use ptython to make a spell checker"
    parts = sentence.split(" ")
    
    suggestions = {}
    for word in parts:
        if word.lower() not in word_list:
            print(f"*{word}* ", end="")
            suggestions[word] = get_close_matches(word, word_list)
        else:
            print(word + " ", end="")
    # print(suggestions)
    
    print("\nsuggestions: ")
    
    for word, values in suggestions.items():
        result = ""
        result += word + ": "
        for value in values:
            result += value + ", "
        print(result[:-2])

        





main()