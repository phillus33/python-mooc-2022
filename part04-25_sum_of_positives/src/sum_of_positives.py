def sum_of_positives(my_list: list) -> int:
    sum = 0
    for number in my_list:
        if number > 0:
            sum += number
    return sum