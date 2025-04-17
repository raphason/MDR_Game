from sqlite3 import Row
from constants import MAX_DIGIT
import random

class Number:
    def __init__(self, row, col):
        self.maximum = MAX_DIGIT
        self.value = self.generate_value();
        self.row = row
        self.col = col
    
    def generate_value(self):
        return random.randint(0, self.maximum)
