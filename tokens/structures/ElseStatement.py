from ..LambdaTypes.Instruction import Instruction
#from ....LambdaBasicScript.main import execute

def execute(instructions: list):
    for instruction in instructions:
        instruction.execute()
        

class ElseStatement(Instruction):
    def __init__(self, instructions: list):
        self.words = Instruction.getNumberOfWordsInInstructionSet(instructions) + 1
        self.instructions = instructions

    def execute(self, stack):
        execute(self.instructions)