import math
from graph import Graph


def HaveTwoPoints(r1, x1, y1, r2, x2, y2):
	if (abs(r1-r2)<math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))) and (math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) <= (r1+r2)):
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
print "***********"
for i in range(0, n-1):
    for j in range(0, n):
                if i!=j:
                        if HaveTwoPoints(rove[i], hiksove[i], yci[i], rove[j], hiksove[j], yci[j]):
                        		helperDict[i].append(j)

print helperDict

graph = Graph(helperDict)
path = graph.find_all_paths(0, n-1)
print(path)

answer = 100000
for x in path:
	if len(x)-1 < answer:
		answer = len(x) - 1

print "The answer: %s"%(answer)






