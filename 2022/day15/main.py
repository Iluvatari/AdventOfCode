import numpy as np

def getManhattanDistance(first: tuple[int, int], second: tuple[int, int]) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

class Sensor:
    def __init__(self, sensorCoords: tuple[int, int], beaconCoords: tuple[int, int]):
        self.coords = sensorCoords
        self.closestBeacon = beaconCoords
        self.distance = getManhattanDistance(self.coords, self.closestBeacon)

    def coversPoint(self, coordToCheck: tuple[int]) -> bool:
        distance = getManhattanDistance(self.coords, coordToCheck)
        return distance <= self.distance

    def pointsCoveredInRow(self, rowToCheck: int) -> set[int]:
        distanceToRow = abs(self.coords[0] - rowToCheck)
        remainingDistance = self.distance - distanceToRow
        minBound = self.coords[1] - remainingDistance
        maxBound = self.coords[1] + remainingDistance
        pointsCovered = set(range(minBound, maxBound + 1))
        return pointsCovered

def processInput(fileText: list[str]):
    sensors = []
    #beaconCoords = []
    minCol = 100000
    minRow = 100000
    maxCol = 0
    maxRow = 0
    for currLine in fileText:
        sensorCol = int(currLine.split('Sensor at x=')[1].split(',')[0])
        sensorRow = int(currLine.split('Sensor at x=')[1].split(', y=')[1].split(':')[0])

        beaconCol = int(currLine.split('closest beacon is at x=')[1].split(',')[0])
        beaconRow = int(currLine.split('closest beacon is at x=')[1].split(', y=')[1].split(':')[0])
        minCol = min(minCol, sensorCol - abs(sensorCol - beaconCol))
        maxCol = max(maxCol, sensorCol + abs(sensorCol - beaconCol))

        minRow = min(minRow, sensorRow - abs(sensorRow - beaconRow))
        maxRow = max(maxRow, sensorRow + abs(sensorRow - beaconRow))
        sensors.append(Sensor((sensorRow, sensorCol), (beaconRow, beaconCol)))
    colBounds = (minCol, maxCol)
    rowBounds = (minRow, maxRow)
    return sensors, colBounds, rowBounds

def isABeacon(sensors: list[Sensor], coordToCheck: tuple[int, int]) -> bool:
    isABeacon = False
    for currSensor in sensors:
        if coordToCheck == currSensor.closestBeacon:
            isABeacon = True
            return isABeacon
    return False

def isASensor(sensors: list[Sensor], coordToCheck: tuple[int, int]) -> bool:
    isASensor = False
    for currSensor in sensors:
        if coordToCheck == currSensor.coords:
            isASensor = True
            return isASensor
    return False

def checkIfImpossible(sensors: list[Sensor], coord: tuple[int, int]) -> bool:
    for sensor in sensors:
        isCovered = sensor.coversPoint(coord)
        if isCovered:
            break
    return isCovered

fileH = open('input.txt', 'r')
fileText = fileH.readlines()
sensors, colBounds, rowBounds = processInput(fileText)
#ROW_NUM = 10
ROW_NUM = 2000000
#numImpossible = 0
#for currX in range(xBounds[0], xBounds[1] + 1):
#    if isABeacon(sensors, (ROW_NUM, currX)):
#        continue
#    if isASensor(sensors, (ROW_NUM, currX)):
#        continue
#    isImpossible = checkIfImpossible(sensors, (ROW_NUM, currX))
#    if isImpossible:
#        numImpossible += 1
columns = set()
for sensor in sensors:
    pointsCovered = sensor.pointsCoveredInRow(ROW_NUM)
    columns.update(pointsCovered)
toRemove = []
for column in columns:
    if isABeacon(sensors, (ROW_NUM, column)):
        toRemove.append(column)
    if isASensor(sensors, (ROW_NUM, column)):
        toRemove.append(column)
for column in toRemove:
    columns.remove(column)
numImpossible = columns.__len__()
print(numImpossible)   
