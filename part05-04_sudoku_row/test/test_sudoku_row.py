import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.sudoku_row'
function = 'row_correct'

def get_correct(test_case: list) -> int:
    c = [(reduce((lambda x,y: x + y), test_case).count(n), n) for n in (1,2)]
    return max(c)[1] if c[0][0] != c[1][0] else 0

def p(sudoku):
    m = 'sudoku = [\n'
    j = 0
    for row in sudoku:
        s = ', '.join([str(i) for i in row])
        m += f'  [ {s} ],   # rivi {j}\n'
        j += 1
    return m +']'  

@points('5.sudoku_row')
class SudokuRowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Asking input from the user was not expected")]):
           cls.module = load_module(exercise, 'en')

    def test_0_main_program_ok(self):
        ok, line = check_source(self.module)
        message =  """The code for testing the functions should be placed inside
if __name__ == "__main__":
block. The following row should be moved:
"""
        self.assertTrue(ok, message+line)

    def test_1_function_exists(self):
        try:
            from src.sudoku_row import row_correct

        except:
            self.assertTrue(False, f'Your code should contain function named as row_correct(sudoku: list, row_no: int)')
        try:
            row_correct = load(exercise, function, 'en')
            s = sudoku = [
                [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
                [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
                [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
                [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
                [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
                [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
                [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
                [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
                [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
            ]
            row_correct(s, 0)
        except:
            self.assertTrue(False, f'Make sure, that function can be called as follows\n{p(s)}\nrow_correct(sudoku, 0)')

    def test_2_type_of_return_value(self):
        row_correct = load(exercise, function, 'en')
        s = sudoku = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
            [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
        ]
        row = 0
        try:
            val = row_correct(s, row)
        except:
            self.assertFalse(True, f"Make sure, that the function can be called as follows\n{p(s)}\nrow_correct(sudoku, 0)")

        self.assertTrue(type(val) == bool, f"Function {function} does not return boolean value when calling\n{p(s)}\nrow_correct(sudoku, 0)")

    def test_3_functionality(self):
        row_correct = load(exercise, function, 'en')
        s = sudoku = [
            [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
            [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
            [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
            [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
            [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
            [ 0, 0, 7, 8, 0, 3, 9, 6, 6 ],
            [ 3, 0, 1, 0, 0, 0, 0, 0, 3 ],
            [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],
        ]

        for row in [0, 3, 4, 5 ]:
            try:
                val = row_correct(s, row)
            except:
                self.assertFalse(True, f"Make sure, that the function can be called as follows\n{p(s)}\nrow_correct(sudoku, 0)")

            self.assertEqual(val, True, f"The result {val} is incorrect when calling\n{p(s)}\nrow_correct(sudoku, {row})")

        for row in [1, 2, 6, 7, 8]:
            try:
                val = row_correct(s, row)
            except:
                self.assertFalse(True, f"Make sure, that the function can be called as follows\n{p(s)}\nrow_correct(sudoku, 0)")

            self.assertEqual(val, False, f"The result {val} is incorrect when calling\n{p(s)}\nrow_correct(sudoku, {row})")

if __name__ == '__main__':
    unittest.main()
