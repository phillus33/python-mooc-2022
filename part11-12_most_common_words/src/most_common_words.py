from string import punctuation
def most_common_words(filename: str, lower_limit: int):
    
    with open(filename) as file:
        content = file.read()
        content = content.replace("\n", " ")
        for item in punctuation:
            content = content.replace(item, "")
        word_list = content.split(" ")

        # Old approach:
        # word_list = []
        # for line in file:
        #     line = line.replace("\n", "")
        #     line = line.replace(".", "")
        #     line = line.replace(",", "")
        #     words = line.split()
        #     for word in words:
        #         word_list.append(word)
    
    return {word: word_list.count(word) for word in word_list if word_list.count(word) >= lower_limit}
    
# print(most_common_words("comprehensions.txt", 3))