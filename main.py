import sys
import random
from tokens.LambdaTypes.LambdaType import LambdaType
from tokens.LambdaTypes.Instruction import Instruction

from tokens.instructions.printf import printf
from tokens.instructions.printvar import printvar
from tokens.instructions.equals import equals
from tokens.instructions.randint import randint
from tokens.instructions.randomuniform import randomuniform
from tokens.instructions.pop import pop
from tokens.instructions.call import call

from tokens.LambdaTypes.string import string
from tokens.LambdaTypes.func import func
from tokens.LambdaTypes.number import number
from tokens.LambdaTypes.boolean import boolean
from tokens.instructions.init import init


from tokens.structures.IfStatement import IfStatement
from tokens.structures.WhileStatement import WhileStatement
from tokens.structures.End import End
from tokens.structures.ElseStatement import ElseStatement

from util.Stack import Stack


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


stack = Stack()


def execute(instructions: list):
    for instruction in instructions:
        instruction.execute(stack)
    


def dataProcess(data: list) -> list:
    '''
    processes the data and returns a list of objects. Each object represents a specific instruction
    '''
    newList: list = []
    i = 0
    while i < len(data):
        if data[i] == 'print':   
            newList.append(printf(data[i+1]))
            i += 1

        elif data[i] == 'init':
            newList.append(init(data[i+1], data[i+2]))
            i += 2

        elif data[i] == 'printvar':
            newList.append(printvar(data[i+1]))
            i += 1

        elif data[i] == 'randint':
            newList.append(randint(data[i+1], int(data[i+2]), int(data[i+3])))
            i += 3
            
        elif data[i] == 'randomuniform':
            newList.append(randomuniform(data[i+1], float(data[i+2]), float(data[i+3])))
            i += 3

        elif data[i] == 'pop':
            newList.append(pop(data[i+1]))
            i += 1

        elif data[i] == 'equals':
            newList.append(equals(data[i+1], data[i+2], data[i+3]))
            i += 3

        elif data[i] == 'if':
            body: list = dataProcess(data[i+1:])
            newList.append(IfStatement(data[i+1], body))
            i += Instruction.getNumberOfWordsInInstructionSet(body) + 2 # add 2 because of the end instruction at the end of the body
        
        elif data[i] == 'else':
            body: list = dataProcess(data[i+1:])
            newList[-1].elseInstructions = body # add the else instructions to the last if statement
            i += Instruction.getNumberOfWordsInInstructionSet(body) + 1 # add 1 because of the end instruction at the end of the body


        elif data[i] == 'while':
            body: list = dataProcess(data[i+1:])
            newList.append(WhileStatement(data[i+1], body))
            i += Instruction.getNumberOfWordsInInstructionSet(body) + 2

        elif data[i] == 'func':
            body: list = dataProcess(data[i+1:])
            stack.push(func(data[i+1], body))
            i += Instruction.getNumberOfWordsInInstructionSet(body) + 2
            
        elif data[i] == 'call':
            newList.append(call(data[i+1]))
            i += 1

        elif data[i] == 'end':
            return newList
        
        i += 1

    return newList


def main():
    # runtime
    checkError()
    data: list = loadData()
    proccessedData: list = dataProcess(data)
    #print(proccessedData)
    execute(proccessedData)
    # debugging stuff
    # print('--------------------------------------')
    # print(stack)
     


if __name__ == '__main__':
    main()


'''
bugs:
    

ideas:
    - functions
    - while loops


'''



