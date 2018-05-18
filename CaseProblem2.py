import numpy as np

angle = 30
angle = angle / 180 * np.pi
AHomogeneousB = np.array([[np.cos(angle), -np.sin(angle), 0, 10], [np.sin(angle), np.cos(angle), 0, 5], [0, 0, 1, 0], [0, 0, 0, 1]])
BPosition = np.array([3, 7, 0, 1])
BPosition = np.transpose(BPosition)  # Makes B into a Column Vector

APosition = np.dot(AHomogeneousB, BPosition)
print(APosition)
