def mean(my_list: list) -> float:
    return sum(my_list)/len(my_list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)