import RandomGraphGenerator
from Graph import Graph
from HeapSort import heapSort


class Kruskal:

    def __init__(self):
        # Make set
        self.T = None
        self.dad = []
        self.rank = []

    def makeSet(self):
        self.dad.append(-1)
        self.rank.append(0)

    def union(self, r1, r2):
        # merge 2 sets r1 and r2 into a single set
        if self.rank[r1] > self.rank[r2]:
            self.dad[r2] = r1
        elif self.rank[r1] < self.rank[r2]:
            self.dad[r1] = r2
        else:
            self.dad[r1] = r2
            self.rank[r2] += 1

    def find(self, v):
        # Find the set containing v
        r = v
        s = []
        while self.dad[r] != -1:
            s.append(r)
            r = self.dad[r]
        while s:
            self.dad[s.pop()] = r
        return r

    def Kruskal_MST(self, G):
        edges = G.get_edges()
        heapSort(edges)
        for i in range(G.num_vertices):
            self.makeSet()  # appending

        self.T = Graph(G.num_vertices)
        for e in edges:
            ru = self.find(e.u)
            rv = self.find(e.v)
            if ru != rv:
                self.T.add_edge(e.u, e.v, e.w)
                self.union(ru, rv)
        return self.T

    def Kruskal_BW(self, G, s, t):
        MST = self.Kruskal_MST(G)
        color = [0] * G.num_vertices
        path = self.DFS(MST, color, s, t, [])
        #TODO: BW value
        return path

    def DFS(self, G, color, s, t, path):
        color[s] = 1
        path.append(s)
        if s == t:
            return path
        for e in G.graph[s]:
            if color[e.vertex_id] == 0:
                if self.DFS(G, color, e.vertex_id, t, path):
                    return path
        path.pop()


if __name__ == "__main__":
    n = 10
    graph = RandomGraphGenerator.generate_graph(1, n)
    graph.print_graph()
    print()
    kruskal = Kruskal()
    print(kruskal.Kruskal_BW(graph, 0, 9))
