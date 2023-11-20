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

    for _ in range(len(adjacency_matrix) - 1):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if dis[j] > dis[i] + adjacency_matrix[i][j]:
                    dis[j] = dis[i] + adjacency_matrix[i][j]
                    pre[j] = i

    for _ in dis:
        print(_)

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                print("There exists arbitrage opportunity in this currency exchange system.")
                return True

    return False


def prepossess_matrix(matrix):
    np_matrix = np.array(matrix)
    np_matrix = -np.log(np_matrix)
    np.fill_diagonal(np_matrix, 0)
    return np_matrix


if __name__ == '__main__':
    matrix = [[1, 0.651, 0.581], [1.531, 1, 0.952], [1.711, 1.049, 1]]
    numpy_matrix = prepossess_matrix(matrix)
    single_source_detect_negative_cycle(numpy_matrix, 0)

    # matrix = JsonMatrixConvert.get_latest_cached_matrix()
    # numpy_matrix = prepossess_matrix(matrix)
    # detect_negative_cycle(numpy_matrix)
