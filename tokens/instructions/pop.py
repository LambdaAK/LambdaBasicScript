

class pop:
    def __init__(self, name: str):
        self.words = 2
        self.name = name
    def execute(self, stack):
        stack.pop(self.name)