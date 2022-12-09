import numpy as np


def processInput(fileText: list[str]):
    mapping = []
    for currLine in fileText:
        currLine = currLine.replace('\n','')
        lineOut = []
        for currChar in currLine:
            lineOut.append(int(currChar))
        mapping.append(lineOut)
    mapping = np.array(mapping)
    return mapping

def treeIsVisible(mapping, i: int, j: int):
    treeHeight = mapping[i,j]
    if max(mapping[0:i,j]) < treeHeight or max(mapping[i + 1:,j]) < treeHeight or max(mapping[i,0:j]) < treeHeight or max(mapping[i,j + 1:]) < treeHeight:
        return True
    else:
        return False

#def countVisibleTrees(mapping: list[list[int]]):
def countVisibleTrees(mapping):
    visibleTrees = 0
    for i, currRow in enumerate(mapping):
        if i == 0 or i == len(mapping) - 1:
            continue
        for j, currTree in enumerate(currRow):
            if j == 0 or j == len(currRow) - 1:
                continue
            if (treeIsVisible(mapping, i, j)):
                visibleTrees += 1
    visibleTrees += len(mapping) * 2
    visibleTrees += len(mapping[0,:]) * 2
    visibleTrees -= 4 # corners
    return visibleTrees

def countScenicScore(mapping, i, j) -> int:
    treeHeight = mapping[i,j]
    tmp = np.nonzero(np.flip((mapping[0:i,j] - treeHeight) >= 0))
    if len(tmp[0]) == 0:
        treesUp = len(mapping[0:i,j])
    else:
        treesUp = tmp[0][0] + 1
    tmp = np.nonzero((mapping[i + 1:,j] - treeHeight >= 0))
    if len(tmp[0]) == 0:
        treesDown = len(mapping[i + 1:,j])
    else:
        treesDown = tmp[0][0] + 1
    tmp = np.nonzero(np.flip((mapping[i,0:j] - treeHeight) >= 0))
    if len(tmp[0]) == 0:
        treesLeft = len(mapping[i,0:j])
    else:
        treesLeft = tmp[0][0] + 1
    #if treesLeft.count() == 0
    #if treesLeft
    tmp = np.nonzero((mapping[i,j + 1:] - treeHeight >= 0))
    if len(tmp[0]) == 0:
        treesRight = len(mapping[i,j + 1:])
    else:
        treesRight = tmp[0][0] + 1
    scenicScore = treesLeft * treesRight * treesDown * treesUp
    return scenicScore

def findBestTree(mapping: np.array):
    bestScenicScore = 0
    besti = 0
    bestj = 0
    for i, currRow in enumerate(mapping):
        if i == 0 or i == len(mapping) - 1:
            continue
        for j, currTree in enumerate(currRow):
            if j == 0 or j == len(currRow) - 1:
                continue
            scenicScore = countScenicScore(mapping, i, j)
            if scenicScore > bestScenicScore:
                besti = i
                bestj = j
                bestScenicScore = scenicScore
    return (besti, bestj, bestScenicScore)


fileH = open('input.txt','r')
fileText = fileH.readlines()

mapping = processInput(fileText)
visibleTrees = countVisibleTrees(mapping)
print(visibleTrees)

(i,j, bestScore) = findBestTree(mapping)
print(i)
print(j)
print(bestScore)