import numpy as np

angle = 30  # Angle in degrees
angle = 30 / 180 * np.pi  # Angle in radians
ARotateB = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
BPosition = np.array([0, 2, 0])
BPosition = np.transpose(BPosition)  # Makes B into a Column Vector

APosition = np.dot(ARotateB, BPosition)
print(APosition)
