def distinct_numbers(list: list):
    result = []
    list.sort()
    # print(list)
    for item in list:
        if item not in result:
            result.append(item)

    return result

# print(distinct_numbers([3, 2, 1, 3, 2, 1, 3, 2, 1]))
