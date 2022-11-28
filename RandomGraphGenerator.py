import random

from Graph import Graph


def generate_graph(version, num_vertices):
    if version == 1:  # average vertex degree is 6
        return generate_6_degree_graph(num_vertices)
    elif version == 2:  # each vertex is adjacent to about 20% of the other vertices
        return generate_20_percent_graph(num_vertices)
    else:
        print("Version Incorrect")
        return None


def generate_6_degree_graph(num_vertices):
    if (num_vertices <= 6):
        print("ERROR!! Average degree can never reach 6!!")
        return None

    graph = Graph(num_vertices)
    graph = connected_cycle(graph)
    # Degree of each vertex is 2 now

    # Each edge contributes to a degree increment of 2. Adding 2*num_vertices edges will make average degree 6.
    for i in range(2 * num_vertices):
        src, dest, weight = generate_random_edge(num_vertices)
        while not graph.add_edge(src, dest, weight):  # if repeated edge, generate new edge
            src, dest, weight = generate_random_edge(num_vertices)

    if graph.get_average_degree() != 6:
        # To make up for repeated edges:
        print("This should not occur")
        while graph.get_average_degree() < 6:
            src, dest, weight = generate_random_edge(num_vertices)
            graph.add_edge(src, dest, weight)

    return graph


def generate_20_percent_graph(num_vertices):
    graph = Graph(num_vertices)
    graph = connected_cycle(graph)
    neighbour_count = [2] * num_vertices  # Each vertex is connected to 2 other vertices.
    vertices = list(range(num_vertices))
    limit = int(0.2 * num_vertices)
    while True:
        print(neighbour_count)
        src_ind = get_unsatisfying_vertex(vertices, neighbour_count, limit)
        if src_ind is None:
            break
        while neighbour_count[src_ind] < limit:
            dest_ind = generate_random_dest(vertices[src_ind], neighbour_count, vertices, limit)
            if graph.add_edge(vertices[src_ind], vertices[dest_ind], random_weight()):
                neighbour_count[src_ind] += 1
                neighbour_count[dest_ind] += 1
            else:
                if len(neighbour_count) <= 2:
                    neighbour_count[src_ind] = limit
        neighbour_count.pop(src_ind)
        vertices.pop(src_ind)

    return graph


def connected_cycle(graph):
    vertices = list(range(graph.num_vertices))
    random.shuffle(vertices)
    for i in range(len(vertices) - 1):
        graph.add_edge(vertices[i], vertices[i + 1], random_weight())

    # Not necessary:
    graph.add_edge(vertices[len(vertices) - 1], vertices[0], random_weight())
    return graph


def random_weight():
    return random.randint(1, 100)


def generate_random_edge(num_vertices):
    while True:
        i = random.randint(0, num_vertices - 1)
        j = random.randint(0, num_vertices - 1)
        if i != j:
            return i, j, random_weight()


def generate_random_dest(src, neighbour_count, vertices, limit):
    num_vertices = len(neighbour_count)
    while True:
        j = random.randint(0, num_vertices - 1)
        print(j) #TODO FIX INFINITE LOOP
        if src != vertices[j] and neighbour_count[j] < limit:
            return j


def get_unsatisfying_vertex(vertices, neighbour_count, limit):
    index = None
    if len(neighbour_count) == 1:
        return index

    i = 0
    while i < len(neighbour_count):
        if neighbour_count[i] < limit:
            index = i
        else:
            vertices.pop(i)
            neighbour_count.pop(i)
        i += 1
    return index


# cg = generate_graph(2, 20)
# cg.print_graph()
