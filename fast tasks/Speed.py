class Graph(object):
    maxSpeed = -1000
    minSpeed = 1000

    def __init__(self):
        self.g = {}

    def add(self, vertex1, vertex2, weight):
        if vertex1 not in self.g:
            self.g[vertex1] = {}

        if vertex2 not in self.g:
            self.g[vertex2] = {}

        self.g[vertex1][vertex2] = weight
        self.g[vertex2][vertex1] = weight

    def has_link(self, v1, v2):
        return v2 in self[v1] or v1 in self[v2]

    def edges(self):
        data = []

        for from_vertex, destinations in self.g.items():
            for to_vertex, weight in destinations.items():
                if (to_vertex, from_vertex, weight) not in data:
                    data.append((from_vertex, to_vertex, weight))

        return data

    def sorted_by_weight(self, desc=False):
        return sorted(self.edges(), key=lambda x: x[2], reverse=desc)

    def spanning_tree(self, minimum=True):
        mst = Graph()
        parent = {}
        rank = {}

        def find_parent(vertex):
            while parent[vertex] != vertex:
                vertex = parent[vertex]

            return vertex

        def union(root1, root2):
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1

                if rank[root2] == rank[root1]:
                    rank[root2] += 1

        for vertex in self.g:
            parent[vertex] = vertex
            rank[vertex] = 0

        for v1, v2, weight in self.sorted_by_weight(not minimum):
            parent1 = find_parent(v1)
            parent2 = find_parent(v2)

            if parent1 != parent2:
                mst.add(v1, v2, weight)
                union(parent1, parent2)

            if len(self) == len(mst):
                break

        return mst

    def __len__(self):
        return len(self.g.keys())

    def __getitem__(self, node):
        return self.g[node]

    def __iter__(self):
        for edge in self.edges():
            yield edge

    def __str__(self):
        for edge in self.edges():
            if edge[2] < Graph.minSpeed:
                Graph.minSpeed = edge[2]
            elif edge[2] > Graph.maxSpeed:
                Graph.maxSpeed = edge[2]
                print self.maxSpeed
        return "\n".join('from %s to %s: %d' % edge for edge in self.edges())


graph = Graph()

graph.add('1', '3', 2)
graph.add('4', '2', 8)
graph.add('1', '2', 11)
graph.add('1', '4', 3)
graph.add('1', '3', 6)
graph.add('5', '3', 5)
graph.add('3', '6', 9)
graph.add('7', '6', 6)
graph.add('5', '6', 3)
graph.add('2', '5', 7)

print(graph.spanning_tree())
print "Maxspeed: %d ; Minspeed: %d" %(Graph.maxSpeed, Graph.minSpeed)
