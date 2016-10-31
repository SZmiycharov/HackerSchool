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

shoppingList = []

while True:
  try:
     shoppinglistInput = raw_input()
     for i in range(n):
        shoppingList.append(int(shoppinglistInput.split()[i]))
  except StandardError:
     print("Bad input!")
     continue
  else:
     if all(i>10000 or i<1 for i in shoppingList):
         print("shoppingList must be <=10000 and >=1")
         continue
     else:
         break


shoppingListAllCombinations = []
for i in range (1, n):
  numFreeProducts = i/k
  allCombinationsProducts = itertools.combinations(shoppingList, i)
  for subset in allCombinationsProducts:
    shoppingListAllCombinations.append(subset)


currentCombinationProducts = []
fullListProducts = []
okComb = []
totalSum = sum(shoppingList)
bestAnswer = totalSum
currentbestAnswer = totalSum

for i in range(2, n):
  for subset in itertools.combinations(shoppingListAllCombinations, i):
    for products in subset:
      currentCombinationProducts.append(products)

    for product in currentCombinationProducts:
      fullListProducts += product

    if len(fullListProducts) == n-1 and set(fullListProducts) == set(shoppingList):
      for listProducts in currentCombinationProducts:
        freeItems = len(listProducts)/k
        listProducts = sorted(listProducts)
        freeItemsSum = listProducts[0:freeItems]
        for freeItem in freeItemsSum:
          currentbestAnswer -= freeItem
        if currentbestAnswer <= bestAnswer:
          bestAnswer = currentbestAnswer
          
    currentbestAnswer = totalSum     
    fullListProducts = []
    currentCombinationProducts = []

print bestAnswer
