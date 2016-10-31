import sys, getopt
import itertools

while True:
  try:
     nAndk = raw_input()
     n = int(nAndk.split()[0])   
     k = int(nAndk.split()[1])   
  except StandardError:
     print("Bad input!")
     continue
  else:
     if n<1 or n>100000 or k<2 or k>100:
         print("n must be <1 and >100000; k must be <2 and >100")
         continue
     else:
         break

goods = []

while True:
  try:
     allGoods = raw_input()
     for i in range(n):
        goods.append(int(allGoods.split()[i]))
  except StandardError:
     print("Bad input!")
     continue
  else:
     if all(i>10000 or i<1 for i in goods):
         print("goods must be <=10000 and >=1")
         continue
     else:
         break


arrayComb = []
for i in range (1, n):
  numFreeProducts = i/k
  allCombinationsProducts = itertools.combinations(goods, i)
  for subset in allCombinationsProducts:
    arrayComb.append(subset)

# arraycomb - po edini4ki, dvoiki, troiki i t.n

currentComb = []
fullList = []
okComb = []

totalSum = sum(goods)
answer = totalSum
currentAnswer = totalSum

for i in range(2, n):
  for subset in itertools.combinations(arrayComb, i):
    for arr in subset:
      currentComb.append(arr)

    for x in currentComb:
      fullList += x

    if len(fullList) == n-1 and set(fullList) == set(goods):
      for slavi in currentComb:
        freeItems = len(slavi)/k
        slavi = sorted(slavi)
        freeitemssum = slavi[0:freeItems]
        for asd in freeitemssum:
          currentAnswer -= asd
        if currentAnswer <= answer:
          answer = currentAnswer
    currentAnswer = totalSum     
    fullList = []
    currentComb = []

print answer
