def no_shouting(list: list):
    result = []

    for item in list:
        if not item.isupper():
            result.append(item)
    
    return result