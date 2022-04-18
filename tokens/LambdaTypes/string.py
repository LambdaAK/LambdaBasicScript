from ..LambdaTypes.LambdaType import LambdaType


class string(LambdaType):
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'{self.name} = {self.value}'