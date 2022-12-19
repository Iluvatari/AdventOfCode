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
    retVal = int(worryLevel) #Assume first is "old"
    for idx, instrItem in enumerate(instrSplit):
        if (instrItem == "old" or instrItem.isnumeric()):
            continue
        elif (instrItem in ['+', '-', '*', '/']):
            numToOperate = instrSplit[idx + 1]
            if numToOperate == "old":
                numToOperate = int(worryLevel)
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
        global lcm
        for currItem in self.items:
            self.numInspected += 1
            currItem = operate(currItem, self.operation)
            #currItem = int(currItem / 3)
            #currItem = (lcm % currItem) + lcm
            currItem = (currItem % lcm)
            if currItem % self.test.divisibleNum == 0:
                newIdx = self.test.ifTrue
            else:
                newIdx = self.test.ifFalse
            if currRoundNum == 8:
                print('passed to %i' %(newIdx))
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
        
def getDivisor(monkies: list[Monkey]) -> int:
    divisors = []
    for currMonkey in monkies: divisors.append(currMonkey.test.divisibleNum)
    lcm = np.product(np.array(divisors))
    return lcm

fileH = open('input.txt','r')
fileText = fileH.read()
monkies = processInput(fileText)
lcm = int(getDivisor(monkies))
#NUM_ROUNDS = 20    
NUM_ROUNDS = 10000
for currRoundNum in range(0, NUM_ROUNDS):
    simRound(monkies)
    print(currRoundNum)
    #for monkey in monkies: print(monkey.numInspected)
    #print()

allNumInspected = []
for idx, currMonkey in enumerate(monkies): allNumInspected.append(currMonkey.numInspected)
allNumInspected = np.array(allNumInspected, dtype='uint64')
allNumInspected.sort()
print(allNumInspected[-1] * allNumInspected[-2])