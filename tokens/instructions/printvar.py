from ..LambdaTypes.LambdaType import LambdaType
from ..LambdaTypes.Instruction import Instruction

class printvar(Instruction):
    def __init__(self, name: str):
        self.words = 2
        self.name = name
    def execute(self):
        print(stack.get(self.name))