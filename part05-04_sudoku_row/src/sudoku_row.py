def row_correct(sudoku: list, row_no: int): 
    # row = sorted(sudoku[row_no])
    

    # for item in range(len(row)-1):
    #     if row[item] != 0:
    #         if row[item] < 0 or row[item] > 9:
    #             return False
    #         if row[item] == row[item+1]: 
    #             return False
    # return True

    result = []

    for number in sudoku[row_no]:
        if number > 0 and number in result:
            return False
        result.append(number)
    return True

