"""
status:
    -1 : unseen
    0 : fringer
    1 : intree
"""
import RandomGraphGenerator
from Kruskal import Kruskal


def getLargestFringer(status, b_width):
    max_value = -1
    max_fringer = -1
    for i in range(len(status)):
        if status[i] == 0 and max_value < b_width[i]:
            max_value = b_width[i]
            max_fringer = i
    return max_fringer


def Dijkstra_BW(G, s, t):
    status = []
    b_width = []
    dad = []
    fringer_count = 0

    for v in range(G.num_vertices):
        status.append(-1)
        b_width.append(0)
        dad.append(0)

    status[s] = 1
    b_width[s] = 100000  # MAX
    dad[s] = -1

    for e in G.graph[s]:
        status[e.vertex_id] = 0
        fringer_count += 1
        b_width[e.vertex_id] = e.edge_weight
        dad[e.vertex_id] = s

    while fringer_count > 0:
        v = getLargestFringer(status, b_width)
        status[v] = 1
        fringer_count -= 1
        for w in G.graph[v]:
            min_bw = min(b_width[v], w.edge_weight)
            if status[w.vertex_id] == -1:
                status[w.vertex_id] = 0
                fringer_count += 1
                b_width[w.vertex_id] = min_bw
                dad[w.vertex_id] = v
            elif status[w.vertex_id] == 0 and b_width[w.vertex_id] < min_bw:
                b_width[w.vertex_id] = min_bw
                dad[w.vertex_id] = v

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
