def check_haletsky(matrix):
    import numpy as np

    for i in range(len(matrix)):
        chek_matrix = np.full((i + 1, i + 1), 0.0, dtype=float)
        for k in range(i + 1):
            for j in range(i + 1):
                chek_matrix[k][j] = matrix[k][j]
        print(chek_matrix)
        if np.linalg.det(chek_matrix) == 0:
            raise ZeroDivisionError("Деление на ноль запрещено")
