import numpy as np
import re

def getElfFoodTotal(fileText) -> str:
    elfFoodTotal = [0]
    for fileLine in fileText:
        if not re.match(r'^\n$', fileLine):
            elfFoodTotal[-1] += int(fileLine)
        else:
            elfFoodTotal.append(0)
        #print(elfFoodTotal)
    return elfFoodTotal

#fileh = open('input.txt','r')
fileh = open('input.txt','r')
fileText = fileh.readlines()

elfFoodTotal = getElfFoodTotal(fileText)
elfFoodTotalArray = np.array(elfFoodTotal)
maxIdx = np.argmax(elfFoodTotalArray)
print("max idx: %i\n" %(maxIdx))
print("max food: %i\n" %(elfFoodTotal[maxIdx]))

sortedArrayIdc = np.argsort(elfFoodTotalArray)
topList = [elfFoodTotalArray[sortedArrayIdc[-1]], elfFoodTotalArray[sortedArrayIdc[-2]], elfFoodTotalArray[sortedArrayIdc[-3]]]
print(sum(topList))