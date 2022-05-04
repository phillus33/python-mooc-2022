from random import sample

def words(n: int, beginning: str):
    with open("words.txt") as words_file:
        words_list = []
        for line in words_file:
            line = line.replace("\n", "")
            
            if line.startswith(beginning):
                words_list.append(line)
        
        if len(words_list) < n:
            raise ValueError("Not enough words")
        
        return sample(words_list, n)

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)