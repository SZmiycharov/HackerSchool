import math
from graph import Graph

def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

def HaveTwoPoints(r1, x1, y1, r2, x2, y2):
	firstSide = (abs(x2-x1))*(abs(x2-x1))
	secondSide = (abs(y2-y1))*(abs(y2-y1))
	csquared = firstSide + secondSide
	c = math.sqrt(csquared)
	if c < r1+r2:
		return True
	else:
		return False
n = 3
hiksove = []
yci = []
rove = []




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

print hiksove 
helperDict = {}

for i in range(n):
	helperDict[i] = []

for i in range(0, n-1):
	if HaveTwoPoints(rove[i], hiksove[i], yci[i], rove[i+1], hiksove[i+1], yci[i+1]):
		helperDict[i].append(i+1)
print helperDict

graph = Graph(helperDict)

print('The path from vertex 0 to vertex 3:')
path = graph.find_path(0, n-1)
print(path)
if path == None:
	answer = 0
else:
	answer = len(path) - 1

print "THE ANSWER: %s" %(answer)



