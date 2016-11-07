import numpy as np
from algo2 import *
from algoClean import *

import matplotlib.pyplot as plt


# Set up
K = 3
D = 2
N = 225
true_means = np.array([[-1, 1, 0], [1, 1, -1]])

points = np.zeros((D, N))
labels = np.random.randint(0, K, N)


for k in range(K):
	nb = np.sum(labels == k)
	points[:, labels == k] = np.random.multivariate_normal(true_means[:, k], 0.5* np.identity(D), nb).T


#plt.scatter(points[0, :], points[1, :], c=labels, alpha=0.5)
#plt.show()


# Algo
kmean = KMeanClean()
centroids, new_labels = kmean.run(points, K)
print("Kmean done")

plt.scatter(points[0, :], points[1, :], c=new_labels, alpha=0.5)
plt.show()

