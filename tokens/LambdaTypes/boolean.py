from ..LambdaTypes.LambdaType import LambdaType

class boolean(LambdaType):
    def __init__(self, name: str, value: bool):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'{self.name} = {self.value}'