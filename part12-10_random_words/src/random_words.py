from random import randint, choice
def word_generator(characters: str, length: int, amount: int):
    # i determines how many characters per 'word', j determines how many words
    return ("".join(choice(characters) for i in range(length)) for j in range(amount))

    # while amount > 0:
    #     rand = characters[randint(0, len(characters)-1)]
    #     for i in range(length-1):
    #         rand += characters[randint(0, len(characters)-1)]
    #     amount -= 1
    #     yield rand

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)