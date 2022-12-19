import numpy as np

def processInput(fileText: list[str]) -> np.array:
    maxes = [0,0,0]
    for currLine in fileText: #Get bax bounds
        coords = currLine.split(',')
        for idx, axis in enumerate(coords):
            maxes[idx] = max(maxes[idx], int(axis) - 1)
    initArray = np.zeros((maxes[0] + 1, maxes[1] + 1, maxes[2] + 1))
    for currLine in fileText:
        coords = currLine.split(',')
        currCoord = [0,0,0]
        for idx, axis in enumerate(coords):
            currCoord[idx] = int(axis) - 1
        initArray[currCoord[0], currCoord[1], currCoord[2]] = 1
    return initArray

def findSurfaceArea(myMap: np.array):
    dims = myMap.shape
    #for idx, dim in enumerate(dims):
    numInPages = 0
    for currRow in range(0, dims[0]):
        for currCol in range(0, dims[1]):
            numInPage = np.sum(np.abs(np.diff(myMap[currRow, currCol, :]))) + myMap[currRow, currCol, [0]][0] + myMap[currRow, currCol, [-1]][0] #rises or falls, add one for the edge I think?
            numInPages += numInPage
    numInRows = 0
    for currCol in range(0, dims[1]):
        for currPage in range(0, dims[2]):
            numInRow = np.sum(np.abs(np.diff(myMap[:, currCol, currPage]))) + myMap[[0], currCol, currPage][0] + myMap[[-1], currCol, currPage][0] #rises or falls, add one for the edge I think?
            numInRows += numInRow
    numInCols = 0
    for currRow in range(0, dims[0]):
        for currPage in range(0, dims[2]):
            numInCol = np.sum(np.abs(np.diff(myMap[currRow, :, currPage]))) + myMap[currRow, [0], currPage][0] + myMap[currRow, [-1], currPage][0] #rises or falls, add one for the edge I think?
            numInCols += numInCol
    totalNum = numInRows + numInCols + numInPages
    return totalNum

fileH = open('input.txt','r')
fileText = fileH.readlines()
myMap = processInput(fileText)
numEdges = findSurfaceArea(myMap)
print(numEdges)
