def longest(list: list) -> str:
    res = ""
    for item in list:
        if len(item) > len(res):
            res = item
    return res
