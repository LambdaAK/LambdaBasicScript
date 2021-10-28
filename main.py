import sys
import random

#reads the file from a paremeters
# splits each word into a list
def loadData():
    with open(sys.argv[1]) as f:
        data = f.read().split()
    return data

def checkError():
    if len(sys.argv) != 2:
        print("Usage: ./main.py <filename>")
        sys.exit(1)



# superclass
# when a new instruction class is created, append it to a list
class Instruction:
    instructionList = []
    def __init_subclass__(cls):
        Instruction.instructionList.append(cls)





class printf(Instruction):
    def __init__(self, data: list):
        self.data = data
    def execute(self):
        print(self.data)
    def __repr__(self):
        return f'print object for value {self.data}'

# has a name
# has a str value
class string:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'{self.name} = {self.value}'


class number:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
    def __repr__(self):
        return f'{self.name} = {self.value}'

# instruction that adds a new variable to the stack
class init(Instruction):
    def __init__(self, name: str, value: str):
        self.variableName = name
        self.variableValue = value

    def execute(self):
        if self.variableValue.isdigit(): # if it's a number
            stack.push(number(self.variableName, int(self.variableValue)))
        else: # if it's a string
            stack.push(string(self.variableName, self.variableValue))


class printvar(Instruction):
    def __init__(self, name: str):
        self.name = name
    def execute(self):
        print(stack.get(self.name))


# takes two numbers which are bounds for the random integer
# sets a value between the bounds for the random integer
# takes a string value which will be used to name the variable the value is stored in
class randint:
    def __init__(self, name: str, min: int, max: int):
        self.name = name
        self.min = min
        self.max = max
    def execute(self):
        stack.push(number(self.name, random.randint(self.min, self.max)))

class randomuniform:
    def __init__(self, name: str, min: int, max: int):
        self.name = name
        self.min = min
        self.max = max
    def execute(self):
        stack.push(number(self.name, random.uniform(self.min, self.max)))




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
                return item.value
        return 'None'



def dataProcess(data: list) -> list:
    newList: list = []
    for i in range(len(data)):
        if data[i] == 'print':
            newList.append(printf(data[i+1]))
            i += 1
        elif (data[i] == 'init'):
            newList.append(init(data[i+1], data[i+2]))
            i += 2
        elif (data[i] == 'printvar'):
            newList.append(printvar(data[i+1]))
            i += 1
        elif (data[i] == 'randint'):
            print(data[i+1], data[i+2], data[i+3])
            newList.append(randint(data[i+1], int(data[i+2]), int(data[i+3])))
            i += 3
        elif (data[i] == 'randomuniform'):
            newList.append(randomuniform(data[i+1], float(data[i+2]), float(data[i+3])))
            i += 3
        

    return newList

def execute(instructions: list):
    for instruction in instructions:
        instruction.execute()
    

stack = Stack()


def main():
    # runtime
    checkError()
    data: list = loadData()
    proccessedData: list = dataProcess(data)

    execute(proccessedData)
    # debugging stuff
    print('--------------------------------------')
    print(stack)
     


if __name__ == '__main__':
    main()
