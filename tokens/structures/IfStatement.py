from ..LambdaTypes.Instruction import Instruction

class IfStatement(Instruction):
    def __init__(self, condition: str, instructions: list):
        '''
        condition is actually a variable name pointing to a boolean value
        if the value of the variable is set to true at the point of runtime,
        the instructions will be executed in self.instructions
        '''
        self.words = Instruction.getNumberOfWordsInInstructionSet(instructions) + 1
        self.condition = condition
        self.instructions = instructions
        self.elseInstructions = []