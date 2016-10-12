import sys, getopt
import itertools

while True:
  try:
     kAndW = raw_input()
     K = int(kAndW.split()[0])   
     W = int(kAndW.split()[1])   
  except StandardError:
     print("Bad input!")
     continue
  else:
     if K<1 or K>15 or W<1 or W>30:
         print("K must be >=1 and <=15")
         continue
     else:
         break

while True:
  try:
     kAndW = raw_input()
     A1 = int(kAndW.split()[0])   
     B1 = int(kAndW.split()[1])
     A2 = int(kAndW.split()[2])
     B2 = int(kAndW.split()[3])
     A3 = int(kAndW.split()[4])
     B3 = int(kAndW.split()[5])
  except StandardError:
     print("Bad input!")
     continue
  else:
     if A1<1 or A1>10 or A2<1 or A2>10 or A3<1 or A3>10 or B1<1 or B1>15 or B2<1 or B2>15 or B3<1 or B3>15:
         print("A must be >=1 and <=10; B must be >=1 and <=15")
         continue
     else:
         break


currentSum = 0
numWays = 0
acceptableStudents = 0
kilos = 0

#B - u4enicite; A - kilogrami; W-max kg;
students = [[A1,B1], [A2,B2], [A3,B3]]
for L in range(0, len(students)+1):
  for subset in itertools.combinations(students, L):
  	# vsqka vuzmojna kombinaciq!
  	if len(subset) > 0:
		for i in subset:
			print "stud:{} kilos:{}".format(i[1], i[0])
			acceptableStudents += i[1]
			kilos += i[0]
		if acceptableStudents >= K and kilos <= W:
			print "YEAH"
			numWays += 1
		acceptableStudents = 0
		kilos = 0

print "numways: {}".format(numWays)



