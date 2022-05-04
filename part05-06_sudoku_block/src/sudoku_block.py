def block_correct(sudoku: list, row_no: int, column_no: int):
    result = []
    rows = sudoku[row_no:row_no+3]
    
    for row in rows:
        for cell in row[column_no:column_no+3]:
            if cell > 0 and cell in result:
                return False
            result.append(cell)
    return True

