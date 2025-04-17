from constants import MAX_DIGIT
import random

class Number:
    def __init__(self):
        self.maximum = MAX_DIGIT
        self.value = self.generate_value();
    
    def generate_value(self):
        return random.randint(0, self.maximum)
