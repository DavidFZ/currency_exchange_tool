import numpy as np
from util.json_matrix_convert import JsonMatrixConvert


def get_test_matrix_1():
    """
    test case 1

    :return matrix: test case matrix
    """
    return [[1, 0.651, 0.581],
            [1.531, 1, 0.952],
            [1.711, 1.049, 1]]


def get_test_matrix_2():
    """
    test case 2

    :return matrix:  test case matrix
    """
    return [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]


def get_real_world_rate_matrix():
    """
    read cache json and convert to matrix

    :return matrix: real world test matrix
    """
    return JsonMatrixConvert.get_latest_cached_matrix()


def negative_logarithm(matrix):
    """
    do negative logarithm process by using numpy lib

    :param matrix: base matrix

    :return matrix: processed matrix
    """
    np_matrix = np.array(matrix)
    np_matrix = -np.log(np_matrix)
    np.fill_diagonal(np_matrix, 0)
    return np_matrix
