def same_chars(word, index1, index2):
    if index1 >= len(word) or index2 >= len(word):
        return False
    else:
        return word[index1] == word[index2]

if __name__ == "__main__":
    print(same_chars("abc", 0, 3))