
def processInput(fileText: list[str]) -> list[int]:
    retVal = []
    for currLine in fileText:
        tmp = currLine.split('addx ')
        if len(tmp) == 2:
            retVal.append(0)
            retVal.append(int(tmp[1])) #Will be zerofor noop
        else:
            retVal.append(0)
    return retVal

def getLineText(cycles: list[int], startSpritePos: int) -> tuple[str, int]:
    retStr = ""
    x = startSpritePos
    for cycleNum, addX in enumerate(cycles):
        if abs(x - (cycleNum)) <= 1: #Sprite is visible
            retStr += "#"
        else:
            retStr += "."
        x += addX
    return retStr, x

fileH = open('input.txt','r')
fileText = fileH.readlines()
cycles = processInput(fileText)
x = 1
sigStr = 0
sigStrengths = []
for idx, currInstr in enumerate(cycles):
    sigStr = (idx + 1)* x
    x += currInstr
    sigStrengths.append(sigStr)
    #print("%i: %i, %i" %(idx + 1, x, sigStr))

print(sigStrengths[19] + sigStrengths[59] + sigStrengths[99] + sigStrengths[139] + sigStrengths[179] + sigStrengths[219])

image = []
currPos = 1
for cycleGroup in range(0, int(240/40 + 1)):
    tmpImage, currPos = getLineText(cycles[cycleGroup * 40:(cycleGroup + 1) * 40], currPos)
    image.append(tmpImage)
    print(tmpImage)
