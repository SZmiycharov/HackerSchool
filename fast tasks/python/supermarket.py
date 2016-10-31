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


