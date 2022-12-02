import random

import RandomGraphGenerator
from Dijkstra_v1 import Dijkstra_BW_v1
from Dijkstra_v2 import Dijkstra_BW_v2
from Kruskal import Kruskal
import time

if __name__ == "__main__":
    num_pairs_of_graphs = 5
    num_src_dests = 5
    n = 5000
    for i in range(num_pairs_of_graphs):
        G1 = RandomGraphGenerator.generate_graph(1, n)
        # G2 = RandomGraphGenerator.generate_graph(2, n)
        for j in range(num_src_dests):
            src = random.randint(0, n - 1)
            dest = random.randint(0, n - 1)
            while(src!=dest):
                dest = random.randint(0, n - 1)

            start_time = time.time()
            dad, b_width = Dijkstra_BW_v1(G1, src, dest)
            print("---Dijkstra_BW_v1 :  %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
            dad, b_width = Dijkstra_BW_v2(G1, src, dest)
            print("---Dijkstra_BW_v2 :  %s seconds ---" % (time.time() - start_time))
            start_time = time.time()
            kruskal = Kruskal()
            kruskal.Kruskal_BW(G1, src, dest)
            print("---Kruskal_BW :  %s seconds ---" % (time.time() - start_time))
            # dad, b_width = Dijkstra_BW_v1(G2, src, dest)
            # dad, b_width = Dijkstra_BW_v2(G2, src, dest)
            # kruskal = Kruskal()
            # kruskal.Kruskal_BW(G2, src, dest)