def column_correct(sudoku: list, column_no:int) -> bool:
    result = []

    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in result:
            return False
        result.append(row[column_no])
    return True

