import numpy as np

x2d = np.array([[8, 3, 9, 16],
                [20, 4, 1, 6]])

row = np.array([0, 1])
col = np.array([3, 2])
print(x2d[row, col])
