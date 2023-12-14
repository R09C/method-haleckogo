# from haletsky_method.forward_motion import forward_motion
# from haletsky_method.reverse_motion import reverse_motion


def haletsky_method(matrix, matrix_z):
    from tex.forward_motion import forward_motion
    from tex.reverse_motion import reverse_motion
    from tex.check_haletsky import check_haletsky
    import numpy as np

    check_haletsky(matrix)
    B = np.full((len(matrix), len(matrix)), 0.0, dtype=float)
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

    y1 = np.linalg.solve(B, matrix_z)
    # print(y1)

    y = reverse_motion(B, matrix_z)

    # print(y)

    x = forward_motion(C, y)

    x1 = np.linalg.solve(C, y1)
    # print(x)
    # print(x1)

    return x


if __name__ == "__main__":  # тесты
    from tex.forward_motion import forward_motion
    from tex.reverse_motion import reverse_motion
    from tex.generate_matrix import generate_matrix
    import numpy as np

    matrix = np.array(
        [[3, 1, -1, 2], [-5, 1, 3, -4], [2, 0, 1, -1], [1, -5, 3, -3]], dtype=float
    )
    matrix_z = np.array([6, -12, 1, 3], dtype=float)
    x_z = np.linalg.solve(matrix, matrix_z)
    x = haletsky_method(matrix, matrix_z)

    [symmetric_matrix, A_z] = generate_matrix()
    t_z = np.linalg.solve(symmetric_matrix, A_z)
    t = haletsky_method(symmetric_matrix, A_z)
    print(t)
    print(
        "------------------------------------------------------------------------------"
    )
    print(t_z)

    # print(x, x_z)
    # print(B.dot(C))
    # np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
