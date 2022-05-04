def length_of_longest(list: list):
    longest = len(list[0])

    for item in list:
        if len(item) > longest:
            longest = len(item)
    return longest