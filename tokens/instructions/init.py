from ..LambdaTypes.Instruction import Instruction
from ..LambdaTypes.string import string
from ..LambdaTypes.number import number

class init(Instruction):
    def __init__(self, name: str, value: str):
        self.words = 3
        self.variableName = name
        self.variableValue = value

    def execute(self, stack):
        if self.variableValue.isdigit(): # if it's a number
            stack.push(number(self.variableName, int(self.variableValue)))
        elif self.variableValue.lower() == "true": # if it's a boolean
            stack.push(string(self.variableName, True))
        elif self.variableValue.lower() == "false": # if it's a boolean
            stack.push(string(self.variableName, False))
        else: # if it's a string
            stack.push(string(self.variableName, self.variableValue))