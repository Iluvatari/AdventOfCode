import numpy as np

def processInput(fileText: list[str]) -> np.array:
    currX = 0
    currY = 0
    retVal = [np.array([currX, currY])]
    for currLine in fileText:
        dir = currLine.split(' ')[0]
        num = int(currLine.split(' ')[1].replace('\n',''))
        for idx in range(0, num):
            if dir == "R":
                currX += 1
            elif dir == "L":
                currX -= 1
            elif dir == "U":
                currY += 1
            elif dir == "D":
                currY -= 1
            else:
                assert(False)
            retVal.append(np.array([currX, currY]))
    retVal = np.vstack(retVal)
    retVal = retVal + np.abs(np.array(retVal[:,0].min()), np.array(retVal[:,1].min()))
    return retVal


def getTailPos(oldTailPos: np.array, newHeadPos: np.array):
    tmp = newHeadPos - oldTailPos
    newTailPos = np.copy(oldTailPos)
    if abs(tmp[0]) > 1: #is in v different vol
        if abs(tmp[1]) >= 1: #Different rows
            newTailPos += np.array([1 * np.sign(tmp[0]), 1 * np.sign(tmp[1])])
        else: #same row...needs to move col but not row
            newTailPos += np.array([1 * np.sign(tmp[0]), 0])
    elif abs(tmp[1]) > 1: #is in adj ish col, v diff row
        if abs(tmp[0]) >= 1: #Different cols, move diag
            newTailPos += np.array([1 * np.sign(tmp[0]), 1 * np.sign(tmp[1])])
        else: #Needs to move row, but not column
            newTailPos += np.array([0, 1 * np.sign(tmp[1])])
    return newTailPos
    #if np.abs(tmp).max() <= 1:
    #    return oldTailPos
    #elif any(np.abs(tmp) > 1) and any(np.abs(tmp) == 1): #Move diaganol
    #    return oldTailPos + np.array([1*np.sign(tmp[0]),1*np.sign(tmp[1])])
    #elif np.abs(tmp[0]) > 1:
    #    return oldTailPos + np.array([1 * np.sign(tmp[0]),0])
    #elif np.abs(tmp[1]) > 1:
    #    return oldTailPos + np.array([0, 1 * np.sign(tmp[1])])
    #else:
    #    assert(False)


fileH = open('input.txt','r')
fileText = fileH.readlines()
HCoords = processInput(fileText)
width = np.max(HCoords[:,0])
height = np.max(HCoords[:,1])
placesVisited = np.array(np.full((width + 1, height + 1), 0))
currTailPos = HCoords[0,:]
#part 2
numKnots = 10
knotPos = np.array(np.full((numKnots, 2), 0))
knotPos[:, 0] = np.copy(HCoords[0,0])
knotPos[:, 1] = np.copy(HCoords[0,1])
placesVisitedEnd = np.array(np.full((width + 1, height + 1), 0))
#
placesVisited[currTailPos[0], currTailPos[1]] = 1
for idx, currCoord in enumerate(HCoords):
    currTailPos = getTailPos(currTailPos, currCoord)
    placesVisited[currTailPos[0], currTailPos[1]] = 1
    #part 2
    knotPos[0,:] = np.copy(currCoord)
    for idxj, currKnot in enumerate(knotPos):
        if idxj == numKnots - 1:
            continue #This is the head or far tail
        knotPos[idxj + 1, :] = getTailPos(knotPos[idxj + 1, :], currKnot)
    placesVisitedEnd[knotPos[numKnots - 1, 0], knotPos[numKnots - 1, 1]] = 1
    #

print(np.sum(placesVisited))
print(np.sum(placesVisitedEnd))
