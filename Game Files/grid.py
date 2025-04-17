import random
from number import Number
from constants import MAX_DIGIT

class Grid:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.cells = self.generate_grid()

    def generate_grid(self):
        return [Number(x, y) for x in range(self.rows) for y in range(self.cols)]
    
    def display(self):
        for i in range(self.rows):
            current_row = ""
            for j in range(self.cols):
                current_row += str(self.cells[i * self.cols + j].value) + "  "
            print(current_row)