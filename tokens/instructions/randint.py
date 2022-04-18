import random
from ..LambdaTypes.number import number

class randint:
    def __init__(self, name: str, min: int, max: int):
        self.words = 4
        self.name = name
        self.min = min
        self.max = max
    def execute(self):
        stack.push(number(self.name, random.randint(self.min, self.max)))