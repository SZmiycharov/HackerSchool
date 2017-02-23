import itertools
import math
import sys

def validateCoordinate(coordinate):
  return coordinate >= 0 and coordinate <= 1000

def validateDoors(doors):
  return doors >= 0 and doors <= 25

def validatePoints(points):
  return points >= 0 and points <= 1000

def getLengthWay(Ax, Bx, Ay, By):
  return math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By))


coordinatesX = []
coordinatesY = []
penalties = []

while True:
  try:
     line = raw_input()
     Sx = int(line.split(' ')[0])
     Sy = int(line.split(' ')[1])       
     Fx = int(line.split(' ')[2])  
     Fy = int(line.split(' ')[3])  
  except StandardError:
     #print("Not an integer!")
     continue
  else:
     if not validateCoordinate(Sx) or not validateCoordinate(Sy) or not validateCoordinate(Fx) or not validateCoordinate(Fy):
         #print("Incorrect values!")
         continue
     else:
        break


while True:
  try:
     numDoors = int(raw_input())
  except StandardError:
     #print("Not an integer!")
     continue
  else:
     if not validatePoints(int(line.split(' ')[2])) or not validateCoordinate(int(line.split(' ')[0])) or not validateCoordinate(int(line.split(' ')[1])):
         #print("Incorrect values!")
         continue
     else:
        break

coordinatesX.append(Sx)
coordinatesY.append(Sy)

for i in range(numDoors):
  while True:
    try:
       line = raw_input()
       coordinatesX.append(int(line.split(' ')[0]))
       coordinatesY.append(int(line.split(' ')[1]))
       penalties.append(int(line.split(' ')[2]))  
    except StandardError:
       #print("Not an integer!")
       continue
    else:
       if not validatePoints(int(line.split(' ')[2])) or not validateCoordinate(int(line.split(' ')[0])) or not validateCoordinate(int(line.split(' ')[1])):
           #print("Incorrect values!")
           continue
       else:
          break

coordinatesX.append(Fx)
coordinatesY.append(Fy)




resultArr = []
currentResult = 0

tablePossibilities = list(itertools.product ([False, True], repeat = len(coordinatesX) - 2))

tablePossibilities = [[True, True, False]]
lastdoor = 0

for possibility in tablePossibilities:
  #print "\n\ncurrent posibility: {}".format(possibility)
  #print "coordinatex: {}".format(coordinatesX)
  #print "coordinatey: {}".format(coordinatesY)
  #print "pelanties: {}\n".format(penalties)
  counterDoor = 1
  currentResult = 0

  for index in range(len(possibility) + 1):
    if index != len(possibility) and possibility[index]:
      currentResult += 1
      currentResult += getLengthWay(coordinatesX[lastdoor], coordinatesX[counterDoor], coordinatesY[lastdoor], coordinatesY[counterDoor])
      #print "add way between doors: {}".format(getLengthWay(coordinatesX[lastdoor], coordinatesX[counterDoor], coordinatesY[lastdoor], coordinatesY[counterDoor]))
      #print "x0: {}, y1: {}, y1: {}, y1: {}".format(coordinatesX[lastdoor],coordinatesY[lastdoor],coordinatesX[counterDoor],coordinatesY[counterDoor])
      #print "currentresult: {}".format(currentResult)
      lastdoor = counterDoor
    elif index != len(possibility) and not possibility[index]:
      pass
      ##print "door false, increment with penalty: {}".format(penalties[lastdoor])
      currentResult += penalties[index]
    else:
      currentResult += 1
      currentResult += getLengthWay(coordinatesX[lastdoor], coordinatesX[counterDoor], coordinatesY[lastdoor], coordinatesY[counterDoor])
      #print "add way between doors: {}".format(getLengthWay(coordinatesX[lastdoor], coordinatesX[counterDoor], coordinatesY[lastdoor], coordinatesY[counterDoor]))
      #print "x0: {}, y1: {}, y1: {}, y1: {}".format(coordinatesX[lastdoor],coordinatesY[lastdoor],coordinatesX[counterDoor],coordinatesY[counterDoor])
      #print "currentresult: {}".format(currentResult)
    
    counterDoor += 1

  resultArr.append(currentResult)

finalResult = sys.maxint
#print "\nRESULT ARR: {}".format(resultArr)

for result in resultArr:
  if result < finalResult:
    finalResult = result


print "%.3f" % finalResult


