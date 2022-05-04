def everything_reversed(words: list):
    result = []

    for item in words:
        result.append(item[::-1])
    return result[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    