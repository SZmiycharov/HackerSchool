import math
from graph import Graph


def HaveTwoPoints(r1, x1, y1, r2, x2, y2):
	firstSide = (abs(x2-x1))*(abs(x2-x1))
	secondSide = (abs(y2-y1))*(abs(y2-y1))
	csquared = firstSide + secondSide
	c = math.sqrt(csquared)
	if c < r1+r2:
		return True
	else:
		return False

hiksove = []
yci = []
rove = []

while True:
	try:
		n = int(input("Enter n: "))
	except StandardError:
		print("Not an integer!")
		continue
	else:
		if n <= 0:
			continue
		else:
			break 

for i in range(n):
	while True:
		try:
			x = int(input("Enter x%s: "%i))
		except StandardError:
			print("Not an integer!")
			continue
		else:
			break 
	while True:
		try:
			y = int(input("Enter y%s: "%i))
		except StandardError:
			print("Not an integer!")
			continue
		else:
			break
	while True:
		try:
			r = int(input("Enter r%s: "%i))
		except StandardError:
			print("Not an integer!")
			continue
		else:
			break
	hiksove.append(x)
	yci.append(y)
	rove.append(r) 	

helperDict = {}
for i in range(n):
	helperDict[i] = []

for i in range(0, n-1):
	for j in range(0, n):
                if i!=j:
                        if HaveTwoPoints(rove[i], hiksove[i], yci[i], rove[j], hiksove[j], yci[j]):
                                helperDict[i].append(j)
print "***********"
print helperDict

graph = Graph(helperDict)

print('The path from vertex 0 to vertex 3:')
path = graph.find_all_paths(0, n-1)
print(path)

answer = 100000
for x in path:
	if len(x)-1 < answer:
		answer = len(x) - 1

print "The answer: %s"%(answer)






