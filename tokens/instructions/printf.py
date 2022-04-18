from ..LambdaTypes.Instruction import Instruction


class printf(Instruction):
    def __init__(self, data: list):
        self.words = 2
        self.data = data
    def execute(self, stack):
        print(self.data)
    def __repr__(self):
        return f'print object for value {self.data}'