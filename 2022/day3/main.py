
def processInput(fileText: list[str]) -> list[tuple[set, set]]:
    retVal = []
    for line in fileText:
        line = line.replace('\n','')
        lineLen = len(line)
        item1 = set(line[0:int(lineLen/2)])
        item2 = set(line[(int(lineLen/2)):(lineLen)])
        retVal.append((item1,item2))
    return retVal

def calcPriority(currItem) -> int:
    if currItem.isupper():
        cost = ord(currItem) - 64 + 26
    else:
        cost = ord(currItem) - 96
    return cost

def checkForDuplicates(pack: tuple[set, set]):
    cost = 0
    hit = False
    for currItem in pack[0]:
        if currItem in pack[1]:
            #print(currItem)
            if hit:
                print('hit')
            cost += calcPriority(currItem)
            hit = True
    if hit == False:
        print('missed')
    return cost

def checkForGroupDuplicates(threePack: list[set[str]]) -> int:
    list1 = threePack[0][0].union(threePack[0][1])
    list2 = threePack[1][0].union(threePack[1][1])
    list3 = threePack[2][0].union(threePack[2][1])

    for currItem in list1:
        if currItem in list2:
            if currItem in list3:
                cost = calcPriority(currItem)
    return cost



fileH = open('input.txt','r')
fileText = fileH.readlines()
output = processInput(fileText)
myCost = 0

for idx, pack in enumerate(output):
    currCost = checkForDuplicates(pack)
    #print(currCost)
    myCost += currCost
    #print(myCost)
print(myCost)

myCost  =0
for idx,tmp in enumerate(output):
    if idx%3 == 0:
        currCost = checkForGroupDuplicates(output[idx:idx+3])
        myCost += currCost
    #print(myCost)
print(myCost)