import networkx as nx
import itertools


ANSWER = 100000


G=nx.DiGraph()

G.add_edge('1','3',weight=2)
G.add_edge('4','2',weight=8)
G.add_edge('1','2',weight=11)
G.add_edge('1','4',weight=3)
G.add_edge('1','3',weight=6)
G.add_edge('5','3',weight=5)
G.add_edge('3','6',weight=9)
G.add_edge('7','6',weight=6)
G.add_edge('5','6',weight=3)
G.add_edge('2','5',weight=7)


edges = [1, 2, 3, 4, 5, 6, 7]

print G.get_edge_data('1','3')['weight']
print "*****************\n\n\n"


for L in range(0, len(edges)+1):
  for subset in itertools.combinations(edges, L):
    if len(subset) == 2:
        print subset


print "\n\n\n"

T=nx.minimum_spanning_tree(G)
for x in sorted(T.edges(data=True)):
    print x[2]['weight'] #tejest na vsqko rebro
