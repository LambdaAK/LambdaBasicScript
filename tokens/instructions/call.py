from ..LambdaTypes.Instruction import Instruction

class call(Instruction):
    def __init__(self, name: str):
        self.words = 2
        self.name = name
    def execute(self, stack):
        func = stack.get(self.name)
        func.execute()