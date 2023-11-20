from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate
from main import prepossess_matrix


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, v, u, w):
        self.edges.append((v, u, w))

    def bellman_ford(self, src):
        # Initialize distances
        d = [float("Inf")] * (self.V + 1)  # starting from 1
        d[src] = 0

        # Repeat |V| - 1 times
        for _ in range(self.V - 1):
            d_prime = list(d)  # Copy current distances to d'
            # self.print_distances(d) # Print the intermediate distances for d.
            for v, u, w in self.edges:
                d_prime[u] = min(d_prime[u], d[v] + w)

            d = d_prime  # Replace d by d'

        # Print distances
        self.print_distances(d)

    def print_distances(self, dist):
        print("Vertex Distance from Source")
        for i in range(1, len(dist)):  # Start from 1
            print("{0}\t\t{1}".format(i, dist[i]))


# Test Example On Slide 21 (without negative cycle)

graph = Graph(5)
graph.add_edge(1, 2, 6)
graph.add_edge(1, 4, 7)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 4, 8)
graph.add_edge(2, 5, -4)
graph.add_edge(3, 2, -2)
graph.add_edge(4, 3, -3)
graph.add_edge(4, 5, 9)
graph.add_edge(5, 1, 2)
graph.add_edge(5, 3, 7)

# Test Example On Slide 21 (modified with negative cycle)

# graph = Graph(5)
# graph.add_edge(1, 2, 6)
# graph.add_edge(1, 4, 7)
# graph.add_edge(2, 3, 5)
# graph.add_edge(2, 4, 8)
# graph.add_edge(2, 5, -6) #modified
# graph.add_edge(3, 2, -2)
# graph.add_edge(4, 3, -3)
# graph.add_edge(4, 5, 9)
# graph.add_edge(5, 1, 2)
# graph.add_edge(5, 3, 7)

# # Test Example on Slide 11 S=1, A=2, B=3, ..., G=8
# graph = Graph(8)
# graph.add_edge(1, 2, 10)
# graph.add_edge(1, 8, 8)
# graph.add_edge(2, 6, 2)
# graph.add_edge(3, 2, 1)
# graph.add_edge(3, 4, 1)
# graph.add_edge(4, 5, 3)
# graph.add_edge(5, 6, -1)
# graph.add_edge(6, 3, -2)
# graph.add_edge(7, 2, -4)
# graph.add_edge(7, 6, -1)
# graph.add_edge(8, 7, 1)


# cached_rate_matrix = JsonMatrixConvert.get_latest_cached_matrix()
# numpy_matrix = prepossess_matrix(cached_rate_matrix)
#
# currencies = RequestExchangeRate.currencies
# node_size = len(currencies)
#
# graph = Graph(node_size)
# for i in range(node_size):
#     for j in range(node_size):
#         graph.add_edge(i + 1, j + 1, numpy_matrix[i][j])
#
# graph.bellman_ford(1)


graph = Graph(3)
graph.add_edge(1, 1, 1)
graph.add_edge(1, 2, 0.651)
graph.add_edge(1, 3, 0.581)
graph.add_edge(2, 1, 1.531)
graph.add_edge(2, 2, 1)
graph.add_edge(2, 3, 0.952)
graph.add_edge(3, 1, 1.711)
graph.add_edge(3, 2, 1.049)
graph.add_edge(3, 3, 1)

graph.bellman_ford(1)
