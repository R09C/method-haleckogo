def forward_motion(C, y):
    import numpy as np

    len_C = len(C)
    x = np.zeros(len_C, dtype=float)
    for i in range(len_C):
        for j in range(i):
            y[len_C - i - 1] -= C[len_C - i - 1][len_C - j - 1] * x[len_C - j - 1]
        x[len_C - i - 1] = y[len_C - i - 1] / C[len_C - i - 1][len_C - i - 1]
    return x
