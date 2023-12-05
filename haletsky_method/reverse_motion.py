def reverse_motion(B, z):
    import numpy as np

    y = np.zeros(len(B), dtype=float)
    for i in range(len(B)):
        for j in range(i):
            z[i] -= B[i][j] * y[j]
        y[i] = z[i] / B[i][i]
    return y
