
def getEndIndex(commaSplitList: list[str]) -> int:
    endBracketIdx = -1
    ignoreCount = -1 #It will increment one on the first index
    for idxj,item in enumerate(commaSplitList): #Only look at the ones at or after this bracket
        if item.__contains__('['):
            ignoreCount += item.count('[')
        if item.__contains__(']'):
            ignoreCount -= item.count(']')
        if ignoreCount == -1:
            endBracketIdx = idxj
            break
    if endBracketIdx == -1:
        assert(False)
    return endBracketIdx

def parseList(listStrIn: str, currList: list):
    splitList = listStrIn.split(',')
    isParsed = False
    idx = 0
    if len(listStrIn) == 0:
        currList.append(None)
        return
    while not isParsed:
        currItem = splitList[idx]
        if currItem.isdigit():
            currList.append(int(currItem))
        elif currItem.__contains__('['):
            endIndex = getEndIndex(splitList[idx:])
            endIndex += idx
            currList.append([])
            parseList(','.join(splitList[idx:endIndex + 1])[1:-1], currList[-1])
            idx = endIndex
        else:
            assert(False)
        idx += 1
        isParsed = idx == len(splitList)

def processInput(fileText: str) -> list[tuple[list]]:
    retVal = []
    pairs = fileText.split('\n\n')
    lineIsParsed = False
    idx = 0
    for pair in pairs:
        pair = pair.split('\n')
        assert(len(pair) == 2)
        list1 = []
        list2 = []
        parseList(pair[0][1:-1], list1)
        parseList(pair[1][1:-1], list2)
        retVal.append((list1, list2))
        idx += 1
    return retVal

def extractBetween(stringIn: str) -> tuple[str, str, str]:
    tmp = stringIn.split('[')
    before = tmp[0]
    tmp = '['.join(tmp[1:]).split(']')
    between = tmp[0]
    after = ']'.join(tmp[1:])
    return before, between, after

def compareLists(list1: list, list2: list) -> bool:
    isInOrder = None
    if list2 is None:
            isInOrder = False
            return isInOrder
    for idx, ignore in enumerate(list1):
        if list1[idx] is None: #2 is longer
            if list2[idx] is not None:
                isInOrder = True
        elif idx == len(list2): #1 is longer
            isInOrder = False
        elif type(list1[idx]) is int:
            if type(list2[idx]) is int:
                if list1[idx] != list2[idx]:
                    isInOrder = list1[idx] < list2[idx]
            elif list2[idx] is None:
                isInOrder = False #1 is longer than 2
            else: #1 is int, 2 is list
                isInOrder = compareLists([list1[idx]], list2[idx])
        elif list1[idx] is None:
            isInOrder = False
        else: #list1[idx] is list
            if type(list2[idx]) is int:
                if list1[idx][0] is None:
                    isInOrder = True
                else:
                    isInOrder = compareLists(list1[idx], [list2[idx]])
            else:
                isInOrder = compareLists(list1[idx], list2[idx])
        if isInOrder is not None:
            break
    if isInOrder is None: #Haven't determined, so we've gone to the last element
        if (len(list1) < len(list2)):
            isInOrder = True
    return isInOrder

def joinPairs(pairList: tuple[list]) -> list:
    pairsOut = []
    for currPair in pairList:
        pairsOut.append(currPair[0])
        pairsOut.append(currPair[1])
    return pairsOut

fileH = open('input.txt','r')
fileText = fileH.read()
parsedList = processInput(fileText)
isInOrder = []
sum = 0
parsedList = joinPairs(parsedList)
sortedList = []
sortedList.append([[2]])
idxOf2 = 0
sortedList.append([[6]])
idxOf6 = 1
for idx, currElem in enumerate(parsedList):
    idxFound = False
    idxToTest = 0
    while idxToTest < len(sortedList):
        belongsHere = compareLists(parsedList[idx], sortedList[idxToTest])
        if belongsHere:
            break
        idxToTest += 1
    sortedList.insert(idxToTest, parsedList[idx])
    if idxToTest <= idxOf2:
        idxOf2 += 1
    if idxToTest <= idxOf6:
        idxOf6 += 1

    #isInOrder.append(compareLists(currPair[0], currPair[1]))
    #print('%i %s: \n\t%s\n\t%s' %(idx, isInOrder[-1], currPair[0], currPair[1]))
    #if isInOrder[-1]:
    #    sum += 1 + idx
    
print((idxOf2 + 1) * (idxOf6 + 1))