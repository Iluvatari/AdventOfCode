import numpy as np

class Operation:
    def __init__(self, operation: str, operationNum: int):
        self.operation = operation
        self.operationNum = operationNum

class Test:
    def __init__(self, divisibleNum: int, ifTrue: int, ifFalse: int):
        self.divisibleNum = divisibleNum
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse

def operate(worryLevel: int, instruction: str) -> int:
    instrSplit = instruction.split(' ')
    retVal = worryLevel #Assume first is "old"
    for idx, instrItem in enumerate(instrSplit):
        if (instrItem == "old" or instrItem.isnumeric()):
            continue
        elif (instrItem in ['+', '-', '*', '/']):
            numToOperate = instrSplit[idx + 1]
            if numToOperate == "old":
                numToOperate = worryLevel
            else:
                numToOperate = int(numToOperate)
            if (instrItem == '+'):
                retVal += numToOperate
            elif (instrItem == '-'):
                retVal -= numToOperate
            elif (instrItem == '*'):
                retVal *= numToOperate
            elif (instrItem == '/'):
                retVal /= numToOperate
        else:
            assert(False)
    return retVal


class Monkey:
    def __init__(self, monkeyText: list[str]):
        assert(len(monkeyText) == 6)
        monkeyNum = int(monkeyText[0].split(' ')[1].replace(':', ''))
        tmp = monkeyText[1].split(', ')
        tmp[0] = tmp[0].split(': ')[1]
        tmp[-1] = tmp[-1].replace('\n','')
        worryLevels = []
        for item in tmp:
            worryLevels.append(int(item))
        
        operationStr = monkeyText[2].split('= ')[1]
        #operationStr = operationStr.split(' ')
        operation = operationStr

        test = Test(
            int(monkeyText[3].split('divisible by ')[1].replace('\n','')), 
            int(monkeyText[4].split('If true: throw to monkey ')[1].replace('\n','')),
            int(monkeyText[5].split('If false: throw to monkey ')[1].replace('\n',''))
        )

        self.number = monkeyNum
        self.items = worryLevels
        self.operation = operation
        self.test = test
        self.numInspected = 0

    def inspectItems(self, monkies: list):
        for currItem in self.items:
            self.numInspected += 1
            currItem = operate(currItem, self.operation)
            #currItem = int(currItem / 3)
            if currItem % self.test.divisibleNum == 0:
                newIdx = self.test.ifTrue
            else:
                newIdx = self.test.ifFalse
            monkies[newIdx].items.insert(len(monkies[newIdx].items), currItem)
        self.items = []
            
def processInput(fileText: str) -> list[Monkey]:
    fileText = fileText.split('\n\n')
    monkies = []
    for currMonkeyText in fileText:
        currMonkeyText = currMonkeyText.splitlines()
        monkies.append(Monkey(currMonkeyText))
    return monkies

def simRound(monkies: list[Monkey]) -> None:
    for currMonkeyNum in range(0, len(monkies)):
        monkies[currMonkeyNum].inspectItems(monkies)
        


fileH = open('test.txt','r')
fileText = fileH.read()
monkies = processInput(fileText)

#NUM_ROUNDS = 20
NUM_ROUNDS = 10000
for currRoundNum in range(0, NUM_ROUNDS):
    simRound(monkies)
    print(currRoundNum)

allNumInspected = []
for idx, currMonkey in enumerate(monkies): allNumInspected.append(currMonkey.numInspected)
allNumInspected = np.array(allNumInspected)
allNumInspected.sort()
print(allNumInspected[-1] * allNumInspected[-2])