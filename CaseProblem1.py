import numpy as np

ARotateB = np.array([[np.cos(np.pi / 6), -np.sin(np.pi / 6), 0], [np.sin(np.pi / 6), np.cos(np.pi / 6), 0], [0, 0, 1]])
BPosition = np.array([0, 2, 0])
BPosition = np.transpose(BPosition)  # Makes B into a Column Vector

APosition = np.dot(ARotateB, BPosition)
print(APosition)
