class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []  #(u, v, weight)
        self.vertex_data = [''] * size  #vertex names

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight))  #add edge with weight
            
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    '''
    Union Find application:
    1) Sort edges by ascending edge weight
    2) Walk through the sorted edges and look at the edge belongs to,
    if the nodes are already unified we don't include this edge,
    otherwise we include it and unify the nodes.
    3) The algorithm terminates when every edge has been processed or all the vertices have been unified
    '''
    '''
    find(u):
        parent = groupMap.get(u)
        if parent == u:
        return u
        else:
        new_parent = parent.find()
        groupMap.put(u, newParent)

    union(u, v):
        u_par = find(u)
        v_par = find(v) (consider u’s and v’s parents instead)
        if sizeMap.get(u_par) >= sizeMap.get(v_par):
        groupMap.put(v_par, u_par)
        sizeMap.put(u_par, sizeMap.get(u_par) + sizeMap.get(v_par))
        sizeMap.remove(v_par)
        else:
        groupMap.put(u_par, v_par)
        sizeMap.put(v_par, sizeMap.get(u_par) + sizeMap.get(v_par))
        sizeMap.remove(u_par)
    '''

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    '''
    Kruskal(G):
    T = empty set // set to store the resulting minimum spanning tree
    edge_counter = 0
    sort all edges in non-decreasing order of their weights
    
    for each vertex v in G:
        create a singleton set for v

    while edge_counter < len(G.edges):
        if find(u) != find(v):
            add (u, v) to T
            merge(find(u), find(v))

    return T
    '''

    def kruskals_algorithm(self):
        result = []  #MST
        i = 0  #edge counter

        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent, rank = [], []

        for node in range(self.size):
            parent.append(node)
            rank.append(0)

        while i < len(self.edges):
            u, v, weight = self.edges[i]
            i += 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        return result

g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')

#source, destination, weight
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 7)
g.add_edge(0, 4, 8)
g.add_edge(1, 3, 4)
g.add_edge(3, 4, 3)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)

print("Kruskal's Algorithm MST:")
mst_resulst = g.kruskals_algorithm()
print(mst_resulst)
print("Edge \tWeight")
for u, v, weight in mst_resulst:
    print(f"{g.vertex_data[u]}-{g.vertex_data[v]} \t{weight}")