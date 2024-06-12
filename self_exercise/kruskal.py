import networkx as nx
import matplotlib.pyplot as plt

# Fungsi find dalam struktur data disjoint-set untuk mencari simpul representatif dari himpunan yang mengandung simpul u
def find(parent, u):
    # Jika simpul u bukan simpul representatif, rekursi dilakukan untuk mencari simpul representatif
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    # Mengembalikan simpul representatif dari himpunan yang mengandung simpul u
    return parent[u]

# Fungsi union dalam struktur data disjoint-set untuk menggabungkan dua himpunan yang mengandung simpul u dan v
def union(parent, rank, u, v):
    # Menemukan simpul representatif dari himpunan yang mengandung simpul u dan v
    pu, pv = find(parent, u), find(parent, v)
    # Jika simpul u dan v berada dalam himpunan yang sama, penggabungan tidak dilakukan
    if pu == pv:
        return False
    # Jika himpunan yang mengandung simpul u memiliki pangkat lebih tinggi, simpul v bergabung ke himpunan u
    if rank[pu] > rank[pv]:
        parent[pv] = pu
    # Jika himpunan yang mengandung simpul v memiliki pangkat lebih tinggi, simpul u bergabung ke himpunan v
    elif rank[pu] < rank[pv]:
        parent[pu] = pv
    # Jika kedua himpunan memiliki pangkat yang sama, salah satu himpunan dijadikan anak himpunan yang lain dan pangkatnya dinaikkan
    else:
        parent[pv] = pu
        rank[pu] += 1
    return True

# Fungsi kruskal_mst untuk mencari Minimum Spanning Tree menggunakan algoritma Kruskal
def kruskal_mst(graph):
    # Mengambil seluruh edge dari graf dan mengurutkannya berdasarkan bobotnya
    edges = [(u, v, weight) for u in graph for v, weight in graph[u].items()]
    edges.sort(key=lambda x: x[2]) # Mengurutkan edge berdasarkan bobotnya
    print(edges) # Output sementara untuk melihat urutan edge
    # Inisialisasi struktur data disjoint-set untuk merepresentasikan himpunan-himpunan dalam graf
    parent = {node: node for node in graph} # Kamus untuk menyimpan simpul induk dari setiap simpul
    rank = {node: 0 for node in graph} # Kamus untuk menyimpan pangkat setiap himpunan
    mst = [] # Inisialisasi MST sebagai list kosong
    # Memproses setiap edge secara berurutan dari yang paling ringan
    for u, v, weight in edges:
        # Jika edge dapat ditambahkan tanpa membentuk siklus
        if union(parent, rank, u, v):
            mst.append((u, v, weight)) # Tambahkan edge ke MST
            visualize_mst(graph, mst) # Visualisasi MST sementara
    return mst # Mengembalikan MST

# Fungsi untuk visualisasi Minimum Spanning Tree
def visualize_mst(graph, mst_edges):
    # Membuat objek graf dari MST
    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges) # Menambahkan edge-edge dari MST ke graf
    pos = nx.spring_layout(G) # Menentukan layout untuk visualisasi
    # Visualisasi graf dengan node berwarna biru langit, ukuran node 1500, edge berwarna hitam, dan label node berukuran 15
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, edge_color="black", linewidths=1, font_size=15, font_weight="bold")
    labels = nx.get_edge_attributes(G, "weight") # Mengambil atribut bobot dari edge
    # Menampilkan label bobot pada edge-edge MST
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    plt.title("Minimum Spanning Tree") # Menambahkan judul pada visualisasi
    plt.show() # Menampilkan visualisasi graf

# Representasi graf sebagai kamus yang memetakan simpul ke tetangganya beserta bobot edge
graph = {
    "A": {"B": 6, "C": 10},
    "B": {"C": 12, "D": 9, "E": 14},
    "C": {"D": 5, "F": 2},
    "D": {"E": 7, "F": 1},
    "E": {"F": 4, "G": 8},
    "F": {"G": 5},
    "G": {}
}

# Mencari Minimum Spanning Tree menggunakan algoritma Kruskal
mst = kruskal_mst(graph)

# Menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} : Weight {edge[2]}")
