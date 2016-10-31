import sys, getopt
import itertools

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

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


# shoppingListAllCombinations = []

# for subset in itertools.combinations(shoppingList, k):
#   shoppingListAllCombinations.append(subset)


# curlist = []
# helper = shoppingList
# valid = True
# numFreeProducts = 0
# totalsum = sum(shoppingList)
# answer = sum(shoppingList)

discount = 0
total = 0
answer = sum(shoppingList)
import pprint
pprint.pprint(list(chunks(sorted(shoppingList), k)))
for x in list(chunks(sorted(shoppingList), k)):
  x = sorted(x)
  if len(x) >= k:
    num = len(x)/k
    discount = sum(x[0:num])
    total += discount


answer < sum(shoppingList) - total

discount = 0
total = 0
helper = sorted(shoppingList)
helper.reverse()
print helper
for x in list(chunks(helper, k)):
  x = sorted(x)
  if len(x) >= k:
    num = len(x)/k
    discount = sum(x[0:num])
    total += discount


if sum(shoppingList) - total < answer:
  answer = sum(shoppingList) - total

print answer




# for subset in itertools.combinations(shoppingListAllCombinations, n/k):
#   helper = shoppingList[:] 
#   for i in subset:
#     for j in i:
#       try:
#         helper.remove(j)
#       except Exception, e:
#         valid = False
#         break

#   if valid:
#     for groupOfProducts in subset:
#       numFreeProducts = len(groupOfProducts)/k
#       groupOfProducts = sorted(groupOfProducts)
#       totalsum -= sum(groupOfProducts[0:numFreeProducts])
#     if totalsum < answer:
#       answer = totalsum
#     print answer

#   totalsum = sum(shoppingList)
#   valid = True
#   helper = shoppingList

# print answer









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
