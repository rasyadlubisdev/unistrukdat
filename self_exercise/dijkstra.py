import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, finish):
    # Inisialisasi jarak awal
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Inisialisasi queue
    unvisited_nodes = set(graph)

    # Inisialisasi predecessors
    predecessors = {}

    while unvisited_nodes:
        # Pilih node dengan jarak terpendek yang belum dikunjungi
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        # Hentikan jika sudah sampai pada node finish
        if current_node == finish:
            break

        # Periksa tetangga-tetangga dari current_node
        for neighbor, weight in graph[current_node]:
            # Hitung jarak baru
            new_distance = distances[current_node] + weight

            # Jika jarak baru lebih pendek dari jarak sebelumnya
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

        # Tandai current_node sebagai sudah dikunjungi
        unvisited_nodes.remove(current_node)

    # Bangun rute dari finish node ke start node
    path = []
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    path.insert(0, start)

    return path, distances[finish], predecessors

# Fungsi untuk menggambar graf menggunakan networkx dan matplotlib
def draw_graph(graph, shortest_path):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
        for neighbor, weight in graph[node]:
            edge_color = 'red' if (node, neighbor) in shortest_path or (neighbor, node) in shortest_path else 'black'
            G.add_edge(node, neighbor, weight=weight, color=edge_color)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    edge_colors = nx.get_edge_attributes(G, 'color').values()
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Graf adjacency list
graph = {
    "A": [("B", 1), ("C", 3), ("D", 3)],
    "B": [("C", 1), ("D", 2)],
    "C": [("D", 4), ("E", 2)],
    "D": [("E", 3)],
    "E": []
}

start_node = "A"
finish_node = "E"

# Temukan rute terpendek dan jaraknya
shortest_path, shortest_distance, predecessors = dijkstra(graph, start_node, finish_node)

# Bangun rute terpendek dari predecessors
current_node = finish_node
path = []
while current_node != start_node:
    path.insert(0, current_node)
    current_node = predecessors[current_node]
path.insert(0, start_node)

# Gambar graf
draw_graph(graph, path)

# Tampilkan rute terpendek dan jaraknya
print("Shortest Path:", path)
print("Shortest Distance:", shortest_distance)
