class Instruction:
    instructionList = []
    def __init_subclass__(cls):
        Instruction.instructionList.append(cls)
    
    def __repr__(self):
        return self.__class__.__name__


    @staticmethod
    def getNumberOfWordsInInstructionSet(instructions: list):
        count = 0
        for instruction in instructions:
            count += instruction.words
        
        return count