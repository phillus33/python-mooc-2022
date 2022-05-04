def even_numbers(list: list) -> list:
    result = []
    for item in list:
        if item % 2 == 0:
            result.append(item)
    return result