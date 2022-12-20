import numpy as np

def processInput(fileText: list[str]) -> tuple[np.array, int, int]:
    maxVert = 0
    maxHorz = 0
    minVert = 1000000
    minHorz = 1000000
    for currLine in fileText:
        for currNode in currLine.split('->'):
            currVert = int(currNode.split(',')[0])
            currHorz = int(currNode.split(',')[1].replace(' ',''))
            if currVert > maxVert:
                maxVert = currVert
            if currHorz > maxHorz:
                maxHorz = currHorz
            if currVert < minVert:
                minVert = currVert
            if currHorz < minHorz:
                minHorz = currHorz
    if minHorz < 0:
        assert(False)
    if minVert < 0:
        assert(False)
    maxHorz += 1
    maxVert += 1
    inputArr = np.zeros((maxVert, maxHorz))
    prevVert = 0
    prevHorz = 0
    for idxi, currLine in enumerate(fileText):
        for idxj, currNode in enumerate(currLine.split('->')):
            currVert = int(currNode.split(',')[0])
            currHorz = int(currNode.split(',')[1].replace(' ',''))
            if idxj == 0: #first node of the line
                prevVert = currVert
                prevHorz = currHorz
                continue
            inputArr[min(prevVert,currVert):max(prevVert,currVert) + 1, min(prevHorz,currHorz):max(prevHorz,currHorz) + 1] = 1
            prevVert = currVert
            prevHorz = currHorz
            


    return inputArr, minVert, maxVert #let's just say it moves rightward

NUM_DROPPED = 0

def dropSand(caveArr: np.array, sandCoord:tuple[int,int], leftWall: int, rightWall: int):
    global NUM_DROPPED
    global SAND_CAN_FALL
    NUM_DROPPED += 1
    sandCanMove = True
    currCoord = list(sandCoord)
    while sandCanMove:
        if currCoord[1] == np.shape(caveArr)[1] - 1:#fell through
            sandCanMove = False
            continue
        if caveArr[currCoord[0], currCoord[1] + 1] == 0: #"down"
            currCoord[1] += 1
        elif caveArr[currCoord[0] - 1, currCoord[1] + 1] == 0: #"downLeft":
            currCoord[1] += 1
            currCoord[0] -= 1
        elif caveArr[currCoord[0] + 1, currCoord[1] + 1] == 0: #"downRight":
            currCoord[1] += 1
            currCoord[0] += 1
        else:
            sandCanMove = False
    if currCoord[1] == np.shape(caveArr)[1] - 1:
        SAND_CAN_FALL = False
    caveArr[currCoord[0], currCoord[1]] = 2 #Sand at rest
    printArray(caveArr, leftWall, rightWall)
        
def printArray(caveArr, minBound, maxBound):
    global FIRST
    with open('image.txt', mode='w') as printFileH:
        myList = caveArr.copy().transpose().tolist()
        #if not FIRST:
            #numToPrint = len(myList)
            #for idx in range(numToPrint + 1):
                #print('\033[F', end='', file=printFileH)
        #else:
        #    FIRST = False
        for idxi, currRow in enumerate(myList):
            for currRowIdx in range(minBound, maxBound):
                currChar = currRow[currRowIdx]
                if currChar == 0:
                    newChar = '.'
                elif currChar == 1:
                    newChar = '#'
                elif currChar == 2:
                    newChar = 'o'
                else:
                    assert(False)
                myList[idxi][currRowIdx] = newChar
            print(''.join(myList[idxi][minBound:maxBound]), file=printFileH)
        print('', file=printFileH)
    

fileH = open('test.txt','r')
fileText = fileH.readlines()
inputArr, minVert, maxVert = processInput(fileText)
SAND_CAN_FALL = True
COORD = (500,0)
FIRST = True

while SAND_CAN_FALL:
    dropSand(inputArr, COORD, minVert, maxVert)
printArray(inputArr, minVert, maxVert)
print(NUM_DROPPED - 1) #last one didn't make it