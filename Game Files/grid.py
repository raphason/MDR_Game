from number import Number
from constants import ROWS, COLS

class Grid:
    def __init__(self, rows=ROWS, cols=COLS):
        self.rows = rows
        self.cols = cols
        self.cells = self.generate_grid()

    def generate_grid(self):
        """Return one-dimensional array of Number objects with Number.position values ranging from 0 to grid size (rows * cols)"""
        return [Number(pos) for pos in range(self.rows* self.cols)]
    
    def display(self):
        for i in range(self.rows):
            current_row = ""
            for j in range(self.cols):
                current_row += str(self.cells[i * self.cols + j].value) + "  "
            print(current_row)