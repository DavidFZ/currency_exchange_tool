import numpy as np

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate
from util.test_case_genrator import *

currencies = RequestExchangeRate.currencies


def detect_negative_cycle(matrix):
    print()
    # bellman-ford algorithm
    for _ in range(len(matrix)):
        res = single_source_detect_negative_cycle(matrix, _)
        if res[0]:
            cycles = res[1]
            # convert list to set
            cycles = [set(cycle) for cycle in cycles]
            for cycle in cycles:
                print("There exists arbitrage opportunity in this currency exchange system.")
                print(" -> ".join(currencies[i] for i in cycle))
                print("Profit margin is " + str(calculate_profit(cycle, matrix)))
            return
    print("There is no arbitrage opportunity in this currency exchange system.")


def single_source_detect_negative_cycle(adjacency_matrix, source_node_index):
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

    flag = False
    potential_path = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if dis[j] > dis[i] + adjacency_matrix[i][j]:
                flag = True
                potential_path.append(tracking_path(pre, i))

    return flag, potential_path


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
    detect_negative_cycle(matrix)

    # test case 2
    matrix = get_test_matrix_2()
    detect_negative_cycle(matrix)

    # # real world case
    matrix = JsonMatrixConvert.get_latest_cached_matrix()
    detect_negative_cycle(matrix)
