class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    '''
    Procedure Dijkstra(Graph, source):
        Create an empty priority queue Q
        Create a set dist[] and initialize it with infinity for all nodes except the source, which starts with distance 0
        Enqueue source to Q with distance 0
        
        while Q is not empty:
            Dequeue the node u from Q
            For each neighbor v of u:
                Calculate a tentative distance d from source to v as dist[u] + weight(u, v)
                If d < dist[v]:
                    Update the distance of v to d
                    Enqueue v to Q with distance d
        
        Return dist[]
    End Procedure
    '''

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(5)

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

#dijkstra's algorithm from D to all vertices
print("Dijkstra's Algorithm starting from vertex A:\n")
distances = g.dijkstra('A')
print(distances)
for i, d in enumerate(distances):
    print(f"Shortest distance from A to {g.vertex_data[i]}: {d}")