def formatted(list: list) -> list:
    result = []
    
    for item in list:
        result.append(f"{item:.2f}")
    
    return result

# my_list = [1.234, 0.3333, 0.11111, 3.446]
# new_list = formatted(my_list)
# print(new_list)