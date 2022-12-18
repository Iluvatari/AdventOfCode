import numpy as np

def getManhattanDistance(first: tuple[int, int], second: tuple[int, int]) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

class Sensor:
    def __init__(self, sensorCoords: tuple[int, int], beaconCoords: tuple[int, int]):
        self.coords = sensorCoords
        self.closestBeacon = beaconCoords
        self.distance = getManhattanDistance(self.coords, self.closestBeacon)

def processInput(fileText: list[str]):
    sensors = []
    #beaconCoords = []
    minX = 100000
    minY = 100000
    maxX = 0
    maxY = 0
    for currLine in fileText:
        sensorX = int(currLine.split('Sensor at x=')[1].split(',')[0])
        sensorY = int(currLine.split('Sensor at x=')[1].split(', y=')[1].split(':')[0])

        beaconX = int(currLine.split('closest beacon is at x=')[1].split(',')[0])
        beaconY = int(currLine.split('closest beacon is at x=')[1].split(', y=')[1].split(':')[0])
        minX = min(minX, sensorX - abs(sensorX - beaconX))
        maxX = max(maxX, sensorX + abs(sensorX - beaconX))

        minY = min(minY, sensorY - abs(sensorY - beaconY))
        maxY = max(maxY, sensorY + abs(sensorY - beaconY))
        sensors.append(Sensor((sensorY, sensorX), (beaconY, beaconX)))
        #beaconCoords.append((beaconX, beaconY))
    xBounds = (minX, maxX)
    yBounds = (minY, maxY)
    return sensors, xBounds, yBounds

def isCloserThanAnyBeacon(beaconCoords: tuple[int, int], sensors: list[Sensor]) -> bool:
    isCloser = False
    for currSensor in sensors:
        if getManhattanDistance(currSensor.coords, beaconCoords) <= currSensor.distance:
            isCloser = True
            return isCloser 
    return False

def isABeacon(beaconCoords: tuple[int, int], sensors: list[Sensor]) -> bool:
    isABeacon = False
    for currSensor in sensors:
        if beaconCoords == currSensor.closestBeacon:
            isABeacon = True
            return isABeacon
    return False

def findNumberImpossibleBeacon(sensors: list[Sensor], rowIdx: tuple[int, int], xBounds: tuple[int, int]) -> int:
    numPossible = 0
    for currBeaconNum in range(xBounds[0], xBounds[1] + 1):
        if isABeacon((rowIdx, currBeaconNum), sensors):
            continue
        for currSensor in sensors:
            if (rowIdx, currBeaconNum) == (currSensor.coords): #We are at the sensod
                continue
            if isCloserThanAnyBeacon((rowIdx, currBeaconNum), sensors):
                numPossible += 1
                break
    return numPossible

fileH = open('input.txt', 'r')
fileText = fileH.readlines()
sensors, xBounds, yBounds = processInput(fileText)
numPossibles = []
for currRowNum in range(yBounds[0], yBounds[1] + 1):
    numPossibles.append(findNumberImpossibleBeacon(sensors, currRowNum, xBounds))
    print(numPossibles[-1])

print(numPossibles[10 - yBounds[0]])
