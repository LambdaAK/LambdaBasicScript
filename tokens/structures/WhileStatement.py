from ..LambdaTypes.Instruction import Instruction

def execute(instructions: list):
    for instruction in instructions:
        instruction.execute()

class WhileStatement(Instruction):
    def __init__(self, condition: str, instructions: list):
        '''
        condition is actually a variable name pointing to a boolean value
        if the value of the variable is set to true at the point of runtime,
        the instructions will be executed in self.instructions
        '''
        self.words = Instruction.getNumberOfWordsInInstructionSet(instructions) + 1
        self.condition = condition
        self.instructions = instructions
        
    def execute(self, stack):
        while self.condition:
            if stack.get(self.condition): # check if the condition is true, then execute the instructions if it is
                execute(self.instructions)
            else:
                execute(self.elseInstructions)