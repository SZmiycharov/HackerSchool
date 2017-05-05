import itertools
import math
import sys
import copy

def validateN(coordinate):
  return coordinate >= 1 and coordinate <= 100

while True:
  try:
     n = int(raw_input())
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if not validateN(n):
         print("Incorrect values!")
         continue
     else:
        break

word = raw_input()
cubes = []

for i in range(n):
  cubes.append(raw_input())



# cubes = ["ABCDEF", "GHIJKL", "MNOPQL", "STUVWN", "EIUOZK"]
cubescopy = copy.deepcopy(cubes)

counter = 0
toremove = "";
resultIndexes = []

for permutation in list(itertools.permutations(cubes)):
  permutation = list(permutation)
  for char in word:
    for cube in permutation:
      if char in cube:
        # print "number: {}; cube: {}; char: {};".format(cubescopy.index(cube), cube, char)
        resultIndexes.append(cubescopy.index(cube) + 1)
        counter += 1
        toremove = cube
        break

    # print "COUNTER: {}".format(counter)
    permutation.remove(toremove)
  if counter == len(word):
    print "YES"
    print(' '.join(map(str,resultIndexes)))
    sys.exit()
  counter = 0
  resultIndexes = []

  print "NO\n";


