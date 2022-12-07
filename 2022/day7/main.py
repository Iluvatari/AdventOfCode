import copy

fileH = open('input.txt','r')
fileText = fileH.readlines()
global NUM_ABOVE
NUM_BELOW = 0
TOTAL_SUM = 0
NUM_ABOVE = 0
global SIZE_TO_CHECK
#SIZE_TO_CHECK = 100000
#SIZE_TO_CHECK = 8381165
DIRS_ABOVE_SIZE = []
def addFile(fileTree, currLoc: list[str], fileName: list[str], fileSize: int):
    global NUM_ABOVE
    if len(currLoc):
        nextDir = currLoc[-1]
        currLoc.pop()
        if (fileSize is not None): # bottom is not dir, and I'm not at bottom yet
            #if fileTree[nextDir][1] < SIZE_TO_CHECK and fileTree[nextDir][1] + fileSize >= SIZE_TO_CHECK: #is newly big
            #    NUM_ABOVE += 1
            fileTree[nextDir][1] += fileSize
        fileTree[nextDir][0] = addFile(fileTree[nextDir][0], currLoc, fileName, fileSize)
        return fileTree
    else:
        if fileName in fileTree.keys():
            assert(False)
        else:
            if fileSize is None: # is dir
                fileTree[fileName] = [dict(), 0]
            else:
                fileTree[fileName] = fileSize
        return fileTree
            
#def getDirSize(fileTree, dirPath: list[str]):
#    tmp = fileTree
#    for currDir in dirPath:
#        tmp = tmp[currDir]
#        tmp[dirPath]

def getNumBelow(fileTree):
    global NUM_BELOW
    global TOTAL_SUM
    global DIRS_ABOVE_SIZE
    for currKey in fileTree.keys():
        if type(fileTree[currKey]) is list:
            #if fileTree[currKey][1] < SIZE_TO_CHECK:
            if fileTree[currKey][1] > SIZE_TO_CHECK:
                NUM_BELOW += 1
                TOTAL_SUM += fileTree[currKey][1]
                DIRS_ABOVE_SIZE.append((currKey, fileTree[currKey][1]))
            getNumBelow(fileTree[currKey][0])


fileTree = dict()
fileTree['/'] = [dict(), 0]
currLoc = []
for idx, currLine in enumerate(fileText):
    if currLine == "$ ls\n":
        continue
    currLine = currLine.replace('\n','')
    if currLine[0].isdigit():
        fileSize = currLine.split(' ')[0]
        fileName = currLine.split(' ')[1].replace('.','')
        currLocTmp = copy.deepcopy(currLoc)
        currLocTmp.reverse()
        fileTree = addFile(fileTree, currLocTmp, fileName, int(fileSize))
    elif currLine[0:3] == "dir":
        fileName = currLine.split('dir ')[1]
        currLocTmp = copy.deepcopy(currLoc)
        currLocTmp.reverse()
        fileTree = addFile(fileTree, currLocTmp, fileName, None)
    elif currLine[0:4] == "$ cd":
        if currLine == "$ cd ..":
            currLoc.pop()
        elif currLine == "$ cd /":
            currLoc = ['/']
        else: #cd ing down
            currLoc.append(currLine.split('$ cd ')[1])
    else:
        assert(False)

SIZE_TO_CHECK = 30000000 - (70000000 - fileTree['/'][1])
getNumBelow(fileTree)
print(TOTAL_SUM)
print(DIRS_ABOVE_SIZE) #No...I'm not looking manually, you are!
