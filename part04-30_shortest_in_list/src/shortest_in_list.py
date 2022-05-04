def shortest(list: list): 
    shortest = ""

    for str in list:
        if shortest == "" or len(str) < len(shortest):
            shortest = str

    return shortest

# print(shortest(['Alan', 'Steve']))