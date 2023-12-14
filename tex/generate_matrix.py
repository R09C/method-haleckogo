import numpy as np


def generate_matrix(n=50):
    A = np.random.rand(n, n)
    A_z = np.random.rand(n)
    symmetric_matrix = 0.5 * (A + A.T)
    return [symmetric_matrix, A_z]


if __name__ == "__main__":  # тесты
    [symmetric_matrix, A_z] = generate_matrix()
    print(A_z)
