import numpy as np
from algo2 import KMean as KMean



# Set up
K = 3
D = 2
N = 100
mean1 = np.array([[-1], [1]])
mean2 = np.array([[1], [1]])
mean3 = np.array([[0], [-1]])

points = np.zeros([D, N])
labels = np.random.randint(0, K, [1, N])


print(points.shape)

# Generate points