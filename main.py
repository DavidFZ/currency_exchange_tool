import numpy as np

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate


def detect_negative_cycle(currencies, matrix):
    # bellman-ford algorithm
    for i in range(len(currencies)):
        dis = [float("inf")] * len(currencies)
        dis[i] = 0
        pre = [-1] * len(currencies)

        for i in range(len(currencies)):
            for j in range(len(currencies)):
                if dis[j] > dis[i] + matrix[i][j]:
                    dis[j] = dis[i] + matrix[i][j]
                    pre[j] = i

        for i in range(len(currencies)):
            for j in range(len(currencies)):
                if dis[j] > dis[i] + matrix[i][j]:
                    print("There exists arbitrage opportunity in this currency exchange system.")
                    exit(1)


def detect_negative_cycle(adjacency_matrix, source_node_index):
    # bellman-ford algorithm
    dis = [float("inf")] * len(adjacency_matrix)
    dis[source_node_index] = 0
    pre = [-1] * len(adjacency_matrix)

    for i in range(len(currencies)):
        for j in range(len(currencies)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                dis[j] = dis[i] + adjacency_matrix[i][j]
                pre[j] = i

    for i in range(len(currencies)):
        for j in range(len(currencies)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                print("There exists arbitrage opportunity in this currency exchange system.")
                return True

    return False


if __name__ == '__main__':
    cached_rate_matrix = JsonMatrixConvert.get_latest_cached_matrix()
    currencies = RequestExchangeRate.currencies

    numpy_matrix = np.array(cached_rate_matrix)
    numpy_matrix = -np.log(numpy_matrix)
    np.fill_diagonal(numpy_matrix, 0)

    detect_negative_cycle(currencies, numpy_matrix)
    matrix = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
