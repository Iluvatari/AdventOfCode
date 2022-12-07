import queue

def processInputs(fileText):
    crates = []
    instruct = []

    procFirst = True
    for idx, line in enumerate(fileText):
        numSpaces = 0
        if line == '\n':
            continue
        if procFirst and fileText[idx + 1] == '\n':
            procFirst = False
            continue
        line = line.replace('\n','')
        if procFirst:
            for charIdx, currChar in enumerate(line):
                if currChar == "[" or currChar == "]":
                    continue
                currCrate = int(charIdx/4) + 1 #width of box...1 based. Round down.
                if currCrate > len(crates):
                    crates.append(queue.LifoQueue())
                if currChar == " ":
                    continue
                crates[currCrate - 1].put(currChar)#zero index
        else:
            numBoxes = int(line.split(' from')[0].split('move ')[1])
            source = int(line.split('from ')[1].split(' to')[0])
            dest = int(line.split('to ')[1])
            instruct.append((numBoxes, source, dest))

    #Flip queue
    for crate in crates:
        listTmp = []
        crateLen = crate.qsize()
        for idx in range(0,crateLen):
            listTmp.append(crate.get())
        #listTmp.reverse()
        for idx in range(0,crateLen):
            crate.put(listTmp[idx])

    return (crates, instruct)

def runSim(crates: list[queue.LifoQueue], instructs: tuple[int, int, int]) -> list[queue.LifoQueue]:
    for currInstruct in instructs:
        for idx in range(0, currInstruct[0]):
            tmp = crates[(currInstruct[1] - 1)].get() #zero index
            crates[currInstruct[2] - 1].put(tmp)
    return crates

def runSim2(crates: list[queue.LifoQueue], instructs: tuple[int, int, int]) -> list[queue.LifoQueue]:
    for currInstruct in instructs:
        numBoxes = currInstruct[0]
        listTmp = []
        for idx in range(0, numBoxes):
            listTmp.append(crates[(currInstruct[1] - 1)].get()) #zero index
        listTmp.reverse()
        for idx in range(0, numBoxes):
            crates[currInstruct[2] - 1].put(listTmp[idx])
    return crates
#fileH = open('test.txt','r')
fileH = open('input.txt','r')

fileText = fileH.readlines()
crates,instruct = processInputs(fileText)
#cratesOut = runSim(crates, instruct)
cratesOut = runSim2(crates, instruct)
for currCrate in cratesOut:
    print(currCrate.get())