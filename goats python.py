#!/usr/bin/env python
def MaxSumAtCurrentIteration(helper, boat,length):
    maxPossibleSum = 0;

    for i in range(length-1, -1, -1):
        if (maxPossibleSum + helper[i] <= boat):
                maxPossibleSum += helper[i];
                del helper [i]
                    
        if (maxPossibleSum == boat):
            break
            
    return maxPossibleSum


goats = [26, 7, 10, 30, 5, 4]
result = 0
currentElement = 0
courses = 2
numberOfGoats = 6
goats.sort()

helperList = list(goats)
currentBoat = helperList[numberOfGoats - 1]
summ = sum(helperList)

while True:
    for x in range(0, courses):
        result += MaxSumAtCurrentIteration(helperList, currentBoat, len(helperList))
        
    if (result == summ):
        break
        
    else:
        currentBoat += 1
        helperList = list(goats)
        result = 0

print(currentBoat)
    

