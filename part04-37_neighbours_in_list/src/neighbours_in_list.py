def longest_series_of_neighbours(list: list):
    # longest = 0
    # curr = 0
    # prev = list[0]

    # for item in list:
    #     if item - prev == 1 or item - prev == -1:
    #         curr += 1
    #     else:
    #         curr = 0
    #     prev = item
    #     if curr > longest:
    #             longest = curr
    # return longest +1

    longest = 0
    curr = 0

    for item in range(1, len(list)):
        if abs(list[item] - list[item-1]) == 1:
            curr += 1
        else:
            curr = 0
        longest = max(curr, longest)
    return longest +1
    
# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))
# longest_series_of_neighbours([1, 2])