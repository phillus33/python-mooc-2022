def row_correct(sudoku: list, row_no: int): 

    result = []

    for number in sudoku[row_no]:
        if number > 0 and number in result:
            return False
        result.append(number)
    return True

def column_correct(sudoku: list, column_no:int) -> bool:
    result = []

    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in result:
            return False
        result.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    result = []
    rows = sudoku[row_no:row_no+3]
    
    for row in rows:
        for cell in row[column_no:column_no+3]:
            if cell > 0 and cell in result:
                return False
            result.append(cell)
    return True

def sudoku_grid_correct(sudoku: list): 
    for row in range(len(sudoku)):
        if not row_correct(sudoku, row):
            return False

    for row in sudoku:
        for col in range(len(row)):
            if not column_correct(sudoku, col):
                return False
    
    for row in range(0, len(sudoku), 3):
        for col in range(0, len(sudoku[row]), 3):
            if not block_correct(sudoku, row, col):
                return False

    return True




