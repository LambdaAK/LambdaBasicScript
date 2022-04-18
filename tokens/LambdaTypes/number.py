from ..LambdaTypes.LambdaType import LambdaType
from ..LambdaTypes.Instruction import Instruction

class number(LambdaType):
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'{self.name} = {self.value}'