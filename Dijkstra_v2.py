"""
status:
    -1 : unseen
    0 : fringer
    1 : intree
"""
import RandomGraphGenerator
from Kruskal import Kruskal
from MaxHeap import MaxHeap


def Dijkstra_BW(G, s, t):
    status = []
    b_width = []
    dad = []

    for v in range(G.num_vertices):
        status.append(-1)
        b_width.append(0)
        dad.append(0)

    status[s] = 1
    b_width[s] = 100000  # MAX
    dad[s] = -1
    fringer_heap = MaxHeap(G.num_vertices)

    for e in G.graph[s]:
        status[e.vertex_id] = 0
        b_width[e.vertex_id] = e.edge_weight
        fringer_heap.insert(e.vertex_id, e.edge_weight)
        dad[e.vertex_id] = s

    while fringer_heap.size != 0:
        v = fringer_heap.maximum()
        fringer_heap.delete(v)
        status[v] = 1
        for w in G.graph[v]:
            min_bw = min(b_width[v], w.edge_weight)
            if status[w.vertex_id] == -1:
                status[w.vertex_id] = 0
                b_width[w.vertex_id] = min_bw
                fringer_heap.insert(w.vertex_id, min_bw)
                dad[w.vertex_id] = v
            elif status[w.vertex_id] == 0 and b_width[w.vertex_id] < min_bw:
                fringer_heap.delete(w.vertex_id)
                b_width[w.vertex_id] = min_bw
                dad[w.vertex_id] = v
                fringer_heap.insert(w.vertex_id, min_bw)

    return dad, b_width


if __name__ == "__main__":
    n = 10
    graph = RandomGraphGenerator.generate_graph(1, n)
    graph.print_graph()
    dad, b_width = Dijkstra_BW(graph, 0, 9)
    i = 9
    while i != -1:
        print(i, end=" ")
        i = dad[i]
    kruskal = Kruskal()
    print(kruskal.Kruskal_BW(graph, 0, 9))
