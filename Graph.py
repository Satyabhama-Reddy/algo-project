class Neighbour:
    def __init__(self, vertex_id, edge_weight):
        self.vertex_id = vertex_id
        self.edge_weight = edge_weight

    def __eq__(self, other):
        if self.vertex_id == other.vertex_id:
            return True
        else:
            return False


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [None] * self.num_vertices

    def add_edge(self, src, dest, weight):
        neighbour = Neighbour(dest, weight)
        if self.graph[src] is None:
            self.graph[src] = []
        if neighbour not in self.graph[src]:
            self.graph[src].append(neighbour)
            if self.graph[dest] is None:
                self.graph[dest] = []
            self.graph[dest].append(Neighbour(src, weight))
        else:
            print("Edge not added. Edge from {} to {} already exists".format(src, dest))

    def print_graph(self):
        for i in range(self.num_vertices):
            print("{} : ".format(i), end="")
            if self.graph[i] is not None:
                for ele in self.graph[i]:
                    print(" -> {},{}".format(ele.vertex_id, ele.edge_weight), end="")
            print("\n")


if __name__ == "__main__":
    num_vertices = 5

    graph = Graph(num_vertices)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 1)
    graph.add_edge(0, 3, 3)
    graph.add_edge(0, 3, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 1, 1)

    graph.print_graph()
