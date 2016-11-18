import sys, getopt
import itertools

def findAngleBetweenHands(hour, minutes):
	return abs(0.5*(60*hour + minutes)-6*minutes)

while True:
  try:
     time = raw_input()
     hour = int(time.split(':')[0])  
     minutes = int(time.split(':')[1])   
  except StandardError:
     print("Bad input!")
     continue
  else:
     if hour<1 or hour>12 or minutes<0 or minutes>59:
         print("1<=hour<=12 and 0<=minutes<=59")
         continue
     else:
         break

angleBetweenHands = findAngleBetweenHands(hour, minutes)
if angleBetweenHands > 180:
	angleBetweenHands = 360 - angleBetweenHands

print angleBetweenHands
