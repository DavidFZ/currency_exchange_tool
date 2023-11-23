import matplotlib.pyplot as plt

from util.json_matrix_convert import JsonMatrixConvert
from util.request_exchange_rate import RequestExchangeRate

def plot_matrix(matrix):
    """
    draw matrix diagram

    :param matrix: exchange rate matrix
    """
    plt.matshow(matrix)

    # set the col and row label of the matrix
    col_labels = row_labels = RequestExchangeRate.currencies
    plt.xticks(range(len(matrix)), col_labels)
    plt.yticks(range(len(matrix)), row_labels)

    # set the color of the text
    # plt.imshow(matrix, cmap=plt.cm.Blues)
    import matplotlib.colors
    my_cmap = matplotlib.colors.ListedColormap(['white'])
    plt.imshow(matrix, cmap=my_cmap)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # format the number
            matrix[i][j] = "{:.4f}".format(matrix[i][j])
            plt.text(i, j, matrix[i][j], va='center', ha='center')

    # set resolutions
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    plt.savefig("matrix.png", dpi=100)

    plt.show()
