def MembersInBetweenAreZeros(arr, currentIndex, c):
    areZero = True
    for i in range(c-2):
        if (arr[currentIndex + 1] != 0):
            areZero = False
            break
        currentIndex += currentIndex
    return areZero

def ClearUntilNexOne(arr, currentIndex, n):
    while(True):
        if(arr[currentIndex] == 1):
            break
        else:
            arr[currentIndex] = 1

while True:
  try:
     n = int(input("Enter n: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(n<=0):
         print("Input must be >0 !")
         continue
     else:
         break

while True:
  try:
     a = int(input("Enter a: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(a<=0):
         print("Input must be >0 !")
         continue
     else:
         break

while True:
  try:
     b = int(input("Enter b: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(b<=0):
         print("Input must be >0 !")
         continue
     else:
         break 

print(b)

while True:
  try:
     c = int(input("Enter c: "))       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(c<=0):
         print("Input must be >0 !")
         continue
     else:
         break

print(c)

remainder = n%b
arr = [None] * 100

for i in range(n+1):
    if(i%a == 0):
        arr[i] = 1

for i in range(n,-1,-1):
    if(i%b == remainder):
        arr[i] = 1

nonRedLines = 0

for i in range (n+1):
    if(arr[i] == 1):
        for j in range (i+1, n+1, 1):
            if(arr[j] == 1 and (j-i) != c):
                nonRedLines += j-i
                break
            if(arr[j] == 1):
                break
            
print "Non red lines: %d" %nonRedLines
    
                                 
