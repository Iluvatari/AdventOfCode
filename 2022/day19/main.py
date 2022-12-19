class Blueprint:
    def __init__(self, textIn: str) -> None:
        self.oreRobot = int(textIn.split('Each ore robot costs ')[1].split(' ore')[0])
        self.clayRobot = int(textIn.split('Each clay robot costs ')[1].split(' ore')[0])
        self.obsidianRobot = (int(textIn.split('Each obsidian robot costs ')[1].split(' ore')[0]), 
            int(textIn.split(' ore and ')[1].split(' clay')[0]))
        self.geodeRobot = (int(textIn.split('Each geode robot costs ')[1].split(' ore')[0]), 
            int(textIn.split(' ore and ')[1].split(' obsidian')[0]))

    def getBestPath(self) -> int:
        orePaybackTime = self.oreRobot
        clayTimeToMake = self.clayRobot

def processInput(fileText: list[str]) -> list[Blueprint]:
    blueprints = []
    for currLine in fileText:
        blueprints.append(Blueprint(currLine))
    return blueprints

fileH = open('test.txt','r')
fileText = fileH.readlines()
blueprints = processInput(fileText)

NUM_MINUTES = 24
for currMinute in range(NUM_MINUTES):

