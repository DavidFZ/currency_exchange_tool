import numpy as np

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate
from util.test_case_genrator import *

currencies = RequestExchangeRate.currencies


def detect_negative_cycle(matrix):
    # bellman-ford algorithm
    for _ in range(len(currencies)):
        if single_source_detect_negative_cycle(matrix, _):
            return True
    return False


def single_source_detect_negative_cycle(adjacency_matrix, source_node_index):
    src_rate = adjacency_matrix
    adjacency_matrix = negative_logarithm(adjacency_matrix)

    dis = [float("inf")] * len(adjacency_matrix)
    dis[source_node_index] = 0
    pre = [-1] * len(adjacency_matrix)

    for _ in range(len(adjacency_matrix) - 1):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if dis[j] > dis[i] + adjacency_matrix[i][j]:
                    dis[j] = dis[i] + adjacency_matrix[i][j]
                    pre[j] = i

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                print("There exists arbitrage opportunity in this currency exchange system.")
                cycle = tracking_path(pre, i)
                print(" -> ".join(currencies[i] for i in cycle))
                print("Profit margin is " + str(calculate_profit(cycle, src_rate)))
                return True

    return False


def tracking_path(predecessors, start_node):
    cycle = [start_node]
    current_node = start_node
    while predecessors[current_node] not in cycle:
        current_node = predecessors[current_node]
        cycle.append(current_node)
    cycle = cycle[cycle.index(predecessors[current_node]):]
    cycle = cycle[::-1]
    cycle.append(cycle[0])
    return cycle


def calculate_profit(cycle, src_rate):
    profit = 1
    for i in range(len(cycle) - 1):
        profit *= src_rate[cycle[i]][cycle[i + 1]]
    return profit


if __name__ == '__main__':
    # test case 1
    matrix = get_test_matrix_1()
    single_source_detect_negative_cycle(matrix, 0)

    # test case 2
    matrix = get_test_matrix_2()
    single_source_detect_negative_cycle(matrix, 0)

    # # real world case
    matrix = JsonMatrixConvert.get_latest_cached_matrix()
    detect_negative_cycle(matrix)
