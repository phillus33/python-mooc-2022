def all_the_longest(list: list):

    result = []

    for item in list:
        if result == [] or len(item) > len(result[0]):
            result = [item]
        elif len(item) == len(result[0]):
            result.append(item)
    return result

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']