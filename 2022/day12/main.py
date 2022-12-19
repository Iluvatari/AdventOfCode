import queue

def processInput(fileText: list[str]):
    dimensions = (len(fileText), len(fileText[0]) - 1) #newline
    heightMap = [[0 for i in range(dimensions[1])] for j in range(dimensions[0])]
    
    for idxi, currLine in enumerate(fileText):
        currLine = currLine.replace('\n','')
        for idxj, currChar in enumerate(currLine):
            if currChar == 'S':
                startLoc = (idxi, idxj)
                heightMap[idxi][idxj] = 0
            elif currChar == 'E':
                endLoc = (idxi, idxj)
                heightMap[idxi][idxj] = 25
            else:
                heightMap[idxi][idxj] = ord(currChar) - ord('a')
    return heightMap, dimensions, startLoc, endLoc

class CostMap:
    def __init__(self, heightMap: list[list[int]], dimensions: tuple[int, int], startLoc: tuple[int, int], endLoc: tuple[int, int]):
        self.costMap = [[2**32 for i in range(dimensions[1])] for j in range(dimensions[0])]
        self.startLoc = startLoc
        self.costMap[startLoc[0]][startLoc[1]] = 0
        self.endLoc = endLoc
        #self.nodesToProcess = queue.LifoQueue()
        self.nodesToProcess = queue.PriorityQueue()
        self.nodesToProcess.put((0, (startLoc)))
        self.dimensions = dimensions
        self.heightMap = heightMap

    def checkNextNode(self):
        if self.nodesToProcess.empty(): #Every node mapped...not stopping at end because I'm not prioritizing smallest path
            return True
        currNode = self.nodesToProcess.get()[1]
        for vert in [-1, 0, 1]:
            nextVert = currNode[0] + vert
            if nextVert < 0 or nextVert >= self.dimensions[0]: #Checking off grid
                continue
            for horz in [-1, 0, 1]:
                nextHorz = currNode[1] + horz
                if horz != 0 and vert != 0: #searching diagnonal
                    continue
                if nextHorz < 0 or nextHorz >= self.dimensions[1]: #Checking off grid
                    continue
                if self.heightMap[nextVert][nextHorz] - self.heightMap[currNode[0]][currNode[1]] > 1: #Path can not be reached bc it's too high
                    continue
                if (self.costMap[currNode[0]][currNode[1]] + 1) < self.costMap[nextVert][nextHorz]: #Path is cheaper
                    self.costMap[nextVert][nextHorz] = self.costMap[currNode[0]][currNode[1]] + 1
                    self.nodesToProcess.put((self.costMap[nextVert][nextHorz], (nextVert, nextHorz)))
        return False

def findStartLocs(heightMap: list[list[int]]) -> list[tuple[int, int]]:
    startLocs = []
    for idxi, currRow in enumerate(heightMap):
        for idxj, currCol in enumerate(currRow):
            if currCol == 0:
                startLocs.append((idxi, idxj))
    return startLocs

with open('input.txt','r') as fileH:
    fileText = fileH.readlines()
heightMap, dimensions, startLoc, endLoc = processInput(fileText)
startLocs = findStartLocs(heightMap)
costs = []
for currStartLoc in startLocs:
    #costMap = CostMap(heightMap, dimensions, startLoc, endLoc)
    costMap = CostMap(heightMap, dimensions, currStartLoc, endLoc)
    isComplete = False
    while (not isComplete):
        isComplete = costMap.checkNextNode()
#    for line in costMap.costMap:
#        print(line)
    totalCost = costMap.costMap[costMap.endLoc[0]][costMap.endLoc[1]]
    #print(totalCost)
    costs.append(totalCost)

print()
print(min(costs))

