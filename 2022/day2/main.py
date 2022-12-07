import numpy as np
import re



def processInput(fileText):
    retVal = []
    for line in fileText:
        splitLine = line.split(' ')
        secondItem = splitLine[1].replace('\n','')
        if splitLine[0] == 'A':
            firstVal = 1
        elif splitLine[0] == 'B':
            firstVal = 2
        if splitLine[0] == 'C':
            firstVal = 3
        if secondItem == 'X':
            secondVal = 1
        elif secondItem == 'Y':
            secondVal = 2
        if secondItem == 'Z':
            secondVal = 3
        retVal.append((firstVal, secondVal))
    return retVal

def runSim(matches) -> int:
    totalScore = 0
    for match in matches:
        if match[0] == match[1]:
            totalScore += 3
        elif match[0] < match[1]: #won
            if match[0] + match[1] == 4: #has to wrap around...flip option
                totalScore += 0
            else:
                totalScore += 6
        elif match[0] > match[1]: #lost
            if match[0] + match[1] == 4: #has to wrap around...flip option
                totalScore += 6
            else:
                totalScore += 0

        totalScore += match[1]
    return totalScore

def runSim2(matches):
    totalScore = 0
    for match in matches:
        if match[1] == 2: #draw
            totalScore += 3
            selected = match[0]
        elif match[1] == 3: #won
            totalScore += 6
            selected = (match[0]+1)%3
        elif match[1] == 1: #lost
            totalScore += 0
            selected = (match[0]-1)%3
        if selected == 0:
            selected = 3
        totalScore += selected
    return totalScore

fileH = open('input.txt','r')
fileText = fileH.readlines()
data = processInput(fileText)
output = runSim(data)
print(output)

output = runSim2(data)
print(output)