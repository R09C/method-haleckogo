def sqr_root_method(matrix, matrix_z):
    import numpy as np
    from tex.forward_motion import forward_motion
    from tex.reverse_motion import reverse_motion
    from tex.check_sqr_root import check_sqr_root

    check_sqr_root(matrix)

    n = len(matrix)
    T = np.zeros_like(matrix, dtype=float)

    for i in range(n):
        for j in range(i + 1):
            sum_z = sum(T[i][k] * T[j][k] for k in range(j))

            if i == j:
                T[i][j] = np.sqrt(matrix[i][i] - sum_z)
            else:
                T[i][j] = (matrix[i][j] - sum_z) / T[j][j]
    # print(matrix)
    # print(T @ T.T)
    y1 = np.linalg.solve(T, matrix_z)
    y = reverse_motion(T, matrix_z)
    # print(y1)
    # print(y)
    x1 = reverse_motion(T.T, y1)
    x = reverse_motion(T.T, y)
    # print(x1)
    # print(x)
    return x


if __name__ == "__main__":
    import numpy as np
    from tex.forward_motion import forward_motion
    from tex.reverse_motion import reverse_motion

    matrix = np.array(
        [[10, 1, -0.5, 0.7], [1, 15, 0.5, 4], [-0.5, 0.5, 20, 1], [0.7, 4, 1, 17]],
        dtype=float,
    )
    matrix_z = np.array([11.2, 20.5, 21, 22.7], dtype=float)
    x = sqr_root_method(matrix, matrix_z)
    x1 = np.linalg.solve(matrix, matrix_z)
    # print(x)
    # print(x1)
