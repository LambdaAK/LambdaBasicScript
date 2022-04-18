from ..LambdaTypes.number import number
import random

class randomuniform:
    def __init__(self, name: str, min: int, max: int):
        self.words = 4
        self.name = name
        self.min = min
        self.max = max
    def execute(self, stack):
        stack.push(number(self.name, random.uniform(self.min, self.max)))