import numpy as np

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate

currencies = RequestExchangeRate.currencies


def detect_negative_cycle(matrix):
    # bellman-ford algorithm
    for _ in range(len(currencies)):
        if single_source_detect_negative_cycle(matrix, _):
            return True
    return False


def single_source_detect_negative_cycle(adjacency_matrix, source_node_index):
    dis = [float("inf")] * len(adjacency_matrix)
    dis[source_node_index] = 0
    pre = [-1] * len(adjacency_matrix)

    # for _ in range(len(adjacency_matrix) - 1):
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                dis[j] = dis[i] + adjacency_matrix[i][j]
                pre[j] = i


    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                print("There exists arbitrage opportunity in this currency exchange system.")
                return True

    return False

if __name__ == '__main__':
    # cached_rate_matrix = JsonMatrixConvert.get_latest_cached_matrix()
    # currencies = RequestExchangeRate.currencies
    #
    # numpy_matrix = np.array(cached_rate_matrix)
    # numpy_matrix = -np.log(numpy_matrix)
    # np.fill_diagonal(numpy_matrix, 0)
    #
    # detect_negative_cycle(numpy_matrix)

    matrix = []
