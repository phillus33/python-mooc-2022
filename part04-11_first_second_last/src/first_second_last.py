# def first_word(sentence):
#     i = 0
#     result = ""

#     while sentence[i] != " ":
#         result += sentence[i]
#         i += 1
#     return result

# def second_word(sentence):
#     i = 0
#     while sentence[i] != " ":
#         i += 1
#     i += 1

#     return first_word(sentence[i:] + " ")

# def last_word(sentence):
#     i = len(sentence)-1
#     tmp = ""

#     while i > 0:
#         if sentence[i] == " ":
#             break
#         else:
#             tmp += sentence[i]
#             i -= 1
#     result = tmp[::-1]
    # return result

def find_word(sentence, place):
    i = 0
    word = ""
    counter = 0

    while i < len(sentence):
        if sentence[i] == " ":
            counter += 1
            if counter == place:
                break
            else:
                word = ""
                i += 1
        else:
            word += sentence[i]
            i += 1
    return word

def first_word(sentence):
    return find_word(sentence, 1)
def second_word(sentence):
    return find_word(sentence, 2)
def last_word(sentence):
    return find_word(sentence, 0)

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word(sentence))