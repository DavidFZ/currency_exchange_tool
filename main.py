import numpy as np


# implement power iteration method
def power_iteration(A, num_simulations):
    # randomly initialize the vector
    b_k = np.random.rand(A.shape[1])
    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        # re normalize the vector
        b_k = b_k1 / b_k1_norm
    return b_k


def page_rank_iteration(A, c):
    # randomly initialize the vector
    b_k = np.random.rand(A.shape[1])

    return b_k


if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    print(A)
    print(power_iteration(A, 10))
