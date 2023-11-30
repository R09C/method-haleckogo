import math
import numpy as np


def haletsky_method(matrix, matrix_z):
    import math
    import numpy as np

    eigenvalues = np.linalg.eigvals(matrix)
    determinant = np.linalg.det(matrix)
    t = np.all(eigenvalues > 0)
    if (not np.all(eigenvalues > 0)) or np.all(matrix != matrix.T) or (determinant < 0):
        raise "ошибка в данных"

    # B = np.zeros(len(matrix))
    B = np.full((len(matrix), len(matrix)), 0.0)
    C = np.eye((len(matrix)))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            B[i][0] = matrix[i][0]
            C[0][j] = matrix[0][j] / B[0][0]
            if (i >= j) and (j > 0):
                summ = 0
                for k in range(0, j):
                    summ += B[i][k] * C[k][j]
                B[i][j] = matrix[i][j] - summ
            if (j > i) and (i > 0):
                summ = 0
                for k in range(0, i):
                    summ += B[i][k] * C[k][j]
                    C[i][j] = (1 / B[i][i]) * (matrix[i][j] - summ)
    y = np.linalg.solve(B, matrix_z)
    x = np.linalg.solve(C, y)
    return [B, C, x]


if __name__ == "__main__":  # тесты
    matrix = np.array([[3, 1, -1, 2], [-5, 1, 3, -4], [2, 0, 1, -1], [1, -5, 3, -3]])
    matrix_z = np.array([6, -12, 1, 3])
    x_z = np.linalg.solve(matrix, matrix_z)
    [B, C, x] = haletsky_method(matrix, matrix_z)
    print(x, x_z)
    print(B.dot(C))
