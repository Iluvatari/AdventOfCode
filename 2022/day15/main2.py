import numpy as np

def getManhattanDistance(first: tuple[int, int], second: tuple[int, int]) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

class Sensor:
    def __init__(self, sensorCoords: tuple[int, int], beaconCoords: tuple[int, int]):
        self.coords = sensorCoords
        self.closestBeacon = beaconCoords
        self.distance = getManhattanDistance(self.coords, self.closestBeacon)
        self.left = self.coords[1] - self.distance
        self.right = self.coords[1] + self.distance

        self.top = self.coords[0] + self.distance
        self.bottom = self.coords[0] - self.distance

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

def getArea(left: int, right: int, top: int, bottom: int) -> int:
        a = (right - left) * (top - bottom) / 2
        b = int(a)
        if b != a:
            assert(False)
        return b

def getIntersection(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    
    return retVal

fileH = open('test.txt', 'r')
fileText = fileH.readlines()
sensors, xBounds, yBounds = processInput(fileText)

for sensor in sensors:
    getArea(sensor.left, sensor.right, sensor.top, sensor.bottom)