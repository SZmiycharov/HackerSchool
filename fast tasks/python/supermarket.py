import sys, getopt
import itertools

def flatten(seq,container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s,'__iter__'):
            flatten(s,container)
        else:
            container.append(s)
    return container

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

for subset in itertools.combinations(shoppingList, k):
  shoppingListAllCombinations.append(subset)


curlist = []
helper = shoppingList
valid = True
numFreeProducts = 0
totalsum = sum(shoppingList)
answer = sum(shoppingList)



for subset in itertools.combinations(shoppingListAllCombinations, n/k):
  helper = shoppingList[:] 
  for i in subset:
    for j in i:
      try:
        helper.remove(j)
      except Exception, e:
        valid = False

  if valid:
    for groupOfProducts in subset:
      numFreeProducts = len(groupOfProducts)/k
      groupOfProducts = sorted(groupOfProducts)
      totalsum -= sum(groupOfProducts[0:numFreeProducts])
  if totalsum < answer:
    answer = totalsum

  totalsum = sum(shoppingList)
  valid = True
  helper = shoppingList

print answer


# currentCombinationProducts = []
# fullListProducts = []
# okComb = []
# totalSum = sum(shoppingList)
# bestAnswer = totalSum
# currentbestAnswer = totalSum


# 11 41 4 65 11 90 55 


# for i in range(1, n):
#   for subset in itertools.combinations(shoppingListAllCombinations, i):
#     for products in subset:
#       currentCombinationProducts.append(products)
#     for product in currentCombinationProducts:
#       fullListProducts += product
    
#     if len(fullListProducts) <= n:
#       for listProducts in currentCombinationProducts:
#         freeItems = len(listProducts)/k
#         listProducts = sorted(listProducts)
#         freeItemsSum = listProducts[0:freeItems]

#         for freeItem in freeItemsSum:
#           currentbestAnswer -= freeItem
#         if currentbestAnswer < bestAnswer:
#           bestAnswer = currentbestAnswer
#           print subset
#           print fullListProducts
#           print "\n"

        
#     currentbestAnswer = totalSum     
#     fullListProducts = []
#     currentCombinationProducts = []

# print bestAnswer
