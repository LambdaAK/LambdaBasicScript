from ..LambdaTypes.LambdaType import LambdaType
from ..LambdaTypes.Instruction import Instruction

class func(LambdaType):
    def __init__(self, name: str, body: list):
        self.words = Instruction.getNumberOfWordsInInstructionSet(body)
        self.name = name
        self.value = body

    def __repr__(self):
        return f'{self.name} = {self.value}'
    
    def execute(self, stack):
        for instruction in self.value:
            instruction.execute(stack)