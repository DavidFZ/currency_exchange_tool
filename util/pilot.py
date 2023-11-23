import matplotlib.pyplot as plt

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate

def plot_matrix(matrix):
    plt.matshow(matrix)
    # remove the background color

    # set the line number of the matrix
    # plt.xticks(RequestExchangeRate.currencies)
    # plt.yticks(RequestExchangeRate.currencies)
    plt.imshow(matrix, cmap=plt.cm.Blues)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # format the number
            matrix[i][j] = "{:.4f}".format(matrix[i][j])
            plt.text(i, j, matrix[i][j], va='center', ha='center')
    # set resolution as 1080p
    fig = plt.gcf()
    fig.set_size_inches(19.20, 10.80)
    plt.savefig("matrix.png", dpi=100)
    plt.show()


if __name__ == '__main__':
    plot_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
