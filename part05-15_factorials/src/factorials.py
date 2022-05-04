def factorials(n: int): 
    # dict = {}
    # result = 1

    # for number in range(1, n+1):
        
    #     result *= number
    #     dict[number] = result
    #     number += 1
    # return dict

    dict = {}
    dict[1] = 1

    for i in range(2, n+1):
        dict[i] = dict[i-1] * i
    return dict


# print(factorials(3))