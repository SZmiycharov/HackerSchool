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

currentDiscount = 0
totalcurrentDiscount = 0
answer = sum(shoppingList)

for x in list(chunks(sorted(shoppingList), k)):
  x = sorted(x)
  if len(x) >= k:
    num = len(x)/k
    currentDiscount = sum(x[0:num])
    totalcurrentDiscount += currentDiscount

currentDiscount = 0
totalcurrentDiscount = 0
helperShopList = sorted(shoppingList)
helperShopList.reverse()

for x in list(chunks(helperShopList, k)):
  x = sorted(x)
  if len(x) >= k:
    num = len(x)/k
    currentDiscount = sum(x[0:num])
    totalcurrentDiscount += currentDiscount


answer = sum(shoppingList) - totalcurrentDiscount

print "The answer is: {}".format(answer)
