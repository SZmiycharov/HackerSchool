import networkx as nx

minForAnswer = 10000000
maxForAnswer = -10000000



#N - broi naseleni mesta ; M - broi putishta ; F i T - nodes ; S - skorost na rebroto

maxweight = -1000000
minweight = 1000000
difference = 1000000
currentMax = -100000000
currentMin = 100000000
nodes = []
weights = []
iteration = 0



while True:
  try:
     line = raw_input("Enter N M: ")
     N = int(line.split(' ')[0])
     M = int(line.split(' ')[1])       
  except StandardError:
     print("Not an integer!")
     continue
  else:
     if(N<2 or N>1000 or M<1 or M>10000):
         print("Incorrect values!")
         continue
     else:
        break

for i in range(N):
    nodes.append(i+1)
nodeshelper = nodes[:]

G = nx.MultiDiGraph()

for i in range(M):
    while True:
      try:
         line = raw_input("Enter F T S: ")
         F = int(line.split(' ')[0])
         T = int(line.split(' ')[1])
         S = int(line.split(' ')[2])

         weights.append(S)
         G.add_edge(F, T,weight=S)
      except StandardError:
         print("Not an integer!")
         continue
      else:
         if(F<1 or F>N or T<1 or T>N or S<1 or S>30000):
             print("Incorrect values!")
             continue
         else:
            break

for x in weights:
    for y in weights:
        print "iteration: {}".format(iteration)
        if x<y:
            minweight = x
            maxweight = y
        else:
            minweight = y
            maxweight = x
        H = nx.Graph([(u,v,d) for (u,v,d) in  G.edges(data=True) if d['weight']>=minweight and d['weight']<=maxweight])

        print "edges in H: {}".format(H.edges())
        for h in H.edges():
            try:
                nodeshelper.remove(h[0]) 
            except:
                pass
            try:
                nodeshelper.remove(h[1])
            except:
                pass
        print "nodeshelper: {}".format(nodeshelper)


        if len(nodeshelper) == 0 and nx.edge_connectivity(H):
            print "CONNECTED WITH ALL NODES!!!"
            print len(H.edges())
            for slavi in H.edges():
                for asd in G[slavi[0]][slavi[1]]:
                    weight = G[slavi[0]][slavi[1]][asd]['weight']
                    print "weight: {}".format(weight)
                    if weight > currentMax:
                        currentMax = weight
                    if weight < currentMin:
                        currentMin = weight
            if difference > currentMax - currentMin:
                difference = currentMax - currentMin
                print "NEW DIFFERENCE: {} ; currentMax: {} ; currentMin: {}".format(difference, currentMax, currentMin)
                maxForAnswer = currentMax
                minForAnswer = currentMin      

        currentMin = 1000000
        currentMax = -1000000
        nodeshelper = nodes[:]
        iteration += 1
        print "\n"


print "Minspeed: {} ; Maxspeed: {} ;".format(minForAnswer, maxForAnswer)


