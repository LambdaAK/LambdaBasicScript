from ..LambdaTypes.Instruction import Instruction
from ..LambdaTypes.boolean import boolean

class equals(Instruction):
    def __init__(self, var1: str, var2: str, name: str):
        self.words = 4
        self.var1 = var1
        self.var2 = var2
        self.name = name
    def execute(self, stack):
        if stack.get(self.var1) == stack.get(self.var2):
            stack.push(boolean(self.name, True))
        else:
            stack.push(boolean(self.name, False))