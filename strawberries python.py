

def GoUp(arr, K, L, currentDay, maxDay, indexi, indexj):
        indexi = indexi + 1
        while indexi < K:
                if currentDay >= maxDay:
                        return
                if currentDay <= arr[indexi][indexj]:
                        arr[indexi][indexj] = currentDay
                        indexi = indexi + 1
                        currentDay = currentDay + 1
                else: break

def GoDown(arr, K, L, currentDay, maxDay, indexi, indexj):
        indexi = indexi - 1
        while indexi >= 0:
                if currentDay >= maxDay:
                        return
                if currentDay <= arr[indexi][indexj]:
                        arr[indexi][indexj] = currentDay
                        indexi = indexi - 1
                        currentDay = currentDay + 1
                else: break

def GoLeft(arr, K, L, currentDay, maxDay, indexi, indexj):
        indexj = indexj - 1
        while indexj >= 0:
                if currentDay >= maxDay:
                        return
                if currentDay <= arr[indexi][indexj]:
                        arr[indexi][indexj] = currentDay
                        indexj = indexj - 1
                        currentDay = currentDay + 1
                else: break

def GoRight(arr, K, L, currentDay, maxDay, indexi, indexj):
        indexj = indexj + 1
        while indexj < L:
                if currentDay >= maxDay:
                        return
                if currentDay <= arr[indexi][indexj]:
                        arr[indexi][indexj] = currentDay
                        indexj = indexj + 1
                        currentDay = currentDay + 1
                else: break

count = 0

while True:
  try:
     K = int(input("Enter K: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(K<0):
         print("Input must be >=0 !")
         continue
     else:
         break
while True:
  try:
     L = int(input("Enter L: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(L<0):
         print("Input must be >=0 !")
         continue
     else:
         break
while True:
  try:
     R = int(input("Enter R: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(R<0):
         print("Input must be >=0 !")
         continue
     else:
         break
while True:
  try:
     i1 = int(input("Enter i1: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(i1<0):
         print("Input must be >=0 !")
         continue
     else:
         break
while True:
  try:
     j1 = int(input("Enter j1: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(j1<0):
         print("Input must be >=0 !")
         continue
     else:
         break
        
choice = raw_input("Another point? y or n: ")
if choice == 'y':
        while True:
          try:
             i2 = int(input("Enter i2: "))       
          except StandardError:
             print("Not an integer!")
             continue
          else:
             if(i2<0):
                 print("Input must be >=0 !")
                 continue
             else:
                 break
        while True:
          try:
             j2 = int(input("Enter j2: "))       
          except StandardError:
             print("Not an integer!")
             continue
          else:
             if(j2<0):
                 print("Input must be >=0 !")
                 continue
             else:
                 break

R = R + 2

arr = [[10000 for x in range(K)] for y in range(L)] 

arr[i1][j1] = 1
if i2 != 0 or j2 != 0:
        arr[i2][j2] = 1
        
currentDay = 1
while True:
        for i in range(K):
                for j in range (L):
                        if arr[i][j] == currentDay:
                                GoUp(arr, K, L, currentDay + 1, R, i, j)
                                GoDown(arr, K, L, currentDay + 1, R, i, j)
                                GoLeft(arr, K, L, currentDay + 1, R, i, j)
                                GoRight(arr, K, L, currentDay + 1, R, i, j)
        currentDay = currentDay + 1
        if currentDay >= R: break


for i in range(K):
        for j in range (L):
                if arr[i][j] == 10000:
                        count = count + 1

print('\n'.join([''.join(['{:6}'.format(item) for item in row]) 
      for row in arr]))
                

print(count)




