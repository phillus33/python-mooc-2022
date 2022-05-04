def print_sudoku(sudoku: list):
    
    for row in range(len(sudoku)):

        if row % 3 == 0 and row != 0:
            print("")
        
        
        for cell in range(len(sudoku[row])):
        
            if sudoku[row][cell] == 0:
                sudoku[row][cell] = "_"
            if cell % 3 == 0 and cell != 0:
                print(" ", end="")
            print(sudoku[row][cell], end=" ")
        
        print("")

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

    
