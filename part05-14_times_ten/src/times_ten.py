def times_ten(start_index: int, end_index: int):
    dict = {}
    for index in range(start_index, end_index+1):
        dict[index] = index*10
    return dict

# times_ten(1, 2)