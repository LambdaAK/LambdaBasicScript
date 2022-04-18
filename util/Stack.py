class Stack:
    def __init__(self):
        self.data = []
    def __repr__(self):
        return f'Stack memory: {self.data}'

    def push(self, value):
        self.data.append(value)
    
    def get(self, name):
        for item in self.data:
            if item.name == name:
                if (item.__class__.__name__ == 'func'):
                    return item
                else:
                    return item.value
        return None
    # removes a variable from the stack by its name
    def pop(self, name):
        for item in self.data:
            if item.name == name:
                self.data.remove(item)
                return