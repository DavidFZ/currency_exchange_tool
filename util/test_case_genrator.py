import numpy as np
from util.json_matrix_convert import JsonMatrixConvert


def get_test_matrix_1():
    return [[1, 0.651, 0.581],
            [1.531, 1, 0.952],
            [1.711, 1.049, 1]]


def get_test_matrix_2():
    return [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]


def get_real_world_rate_matrix():
    return JsonMatrixConvert.get_latest_cached_matrix()


def negative_logarithm(matrix):
    np_matrix = np.array(matrix)
    np_matrix = -np.log(np_matrix)
    np.fill_diagonal(np_matrix, 0)
    return np_matrix
