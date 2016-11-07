import numpy as np

class KmeanExceptDHigherThanN(Exception):
    pass

class KMeanClean(object):
    """my k-mean algorithm"""
    def __init__(self):
        super(KMeanClean, self).__init__()
        
    niter = 100;

    def run(self, points, K):
        """ 
            Points a DxN points
            K integer, greater than 0
        """
        # Get size
        D, N = points.shape

        if K >= N:
            raise KmeanExceptDHigherThanN()

        # DxK array initialiezd with random points
        centroids = points[:, np.random.permutation(N)[:K]]

        # Assigments 1xN array
        labels = np.zeros(N)

        for it in np.arange(self.niter):
            # 1. Compute distance to all cluster
            distances = np.sqrt(((points.T - centroids.T[:, np.newaxis])**2).sum(axis=2))       

            # 2. Update assigments
            labels = np.argmin(distances, axis=0)

            # 3. Update mean
            centroids = np.array([points[:, labels==k].mean(axis=1) for k in range(3)]).T

        return centroids, labels
