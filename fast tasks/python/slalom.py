def validateCoordinate(coordinate):
  return coordinate >= 0 and coordinate <= 1000

def validateDoors(doors):
  return doors >= 0 and doors <= 25

def validatePoints(points):
  return points >= 0 and points <= 1000

while True:
  try:
     line = raw_input()
     Sx = int(line.split(' ')[0])
     Sy = int(line.split(' ')[1])       
     Fx = int(line.split(' ')[2])  
     Fy = int(line.split(' ')[3])  
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if not validateCoordinate(Sx) or not validateCoordinate(Sy) or not validateCoordinate(Fx) or not validateCoordinate(Fy):
         print("Incorrect values!")
         continue
     else:
        break

numDoors = int(raw_input())
coordinatesX = []
coordinatesY = []
penalties = []

for i in range(numDoors):
  while True:
    try:
       line = raw_input()
       coordinatesX.append(int(line.split(' ')[0]))
       coordinatesY.append(int(line.split(' ')[1]))
       penalties.append(int(line.split(' ')[2]))  
    except StandardError:
       print("Not an integer!")
       continue
    else:
       if not validatePoints(int(line.split(' ')[2])) or not validateCoordinate(int(line.split(' ')[0])) or not validateCoordinate(int(line.split(' ')[1])):
           print("Incorrect values!")
           continue
       else:
          break


print "coordinatex: {}".format(coordinatesX)
print "coordinatey: {}".format(coordinatesY)
print "pelanties: {}".format(penalties) 