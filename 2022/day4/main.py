import re
def processInput(assignmentsIn: list[str]) -> list[tuple[set,set]]:
    retVal = []
    for currLine in assignmentsIn:
        currLine = currLine.replace('\n','')
        currLine = currLine.split(',')

        lowBound = int(currLine[0].split('-')[0])
        upperBound = int(currLine[0].split('-')[1])
        set1 = set(range(lowBound, upperBound + 1))

        lowBound = int(currLine[1].split('-')[0])
        upperBound = int(currLine[1].split('-')[1])
        set2 = set(range(lowBound, upperBound + 1))
        retVal.append((set1, set2))
    return retVal

def checkForDuplicates(assignment: tuple[set,set]) -> int:
    duplicate = assignment[0].intersection(assignment[1])
    numDuplicates = len(duplicate)
    #Use commented code for part 1
    #if (numDuplicates == len(assignment[0])) or (numDuplicates == len(assignment[1])):
    #    numFullyContained = 1
    #else:
    #    numFullyContained = 0
    return numDuplicates
    #return numFullyContained

fileH = open('input.txt','r')
fileText = fileH.readlines()
parsedInput = processInput(fileText)
cnt = 0
for currAssignment in parsedInput:
    numDuplicates = checkForDuplicates(currAssignment)
    if numDuplicates:
        cnt += 1

print(cnt)