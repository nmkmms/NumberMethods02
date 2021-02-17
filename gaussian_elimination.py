import numpy as np
from copy import deepcopy


def gaussian(matrix):
    matrix = deepcopy(matrix)
    height, width = matrix.shape

    for i in range(height):
        matrix[i] /= matrix[i, i]
        for j in range(height):
            if i == j:
                continue
            matrix[j] -= matrix[i] * matrix[j, i]
    return matrix[:, -1]


if __name__ == '__main__':
    A = np.array([
        [5, 3, 2, 10],
        [4, 0, 2, 8],
        [1, 2, 3, 4]],
        dtype=float
    )
    res = gaussian(A)
    print(f'Given matrix A = \n{A}\nResult for matrix A:\n{res}')
    print(f'With built-in numpy function:\n{np.linalg.solve(A[:, :-1], A[:, -1])}')
