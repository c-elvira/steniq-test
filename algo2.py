import numpy as np

class KMean(object):
    """my k-mean algorithm"""
    def __init__(self, arg):
        super(KMean, self).__init__()
        self.arg = arg
        
    niter = 100;

    def run(self, points, K):
        """ 
            Points a DxN points
            K integer, greater than 0
        """
        # Get size
        D, N = points.shape

        # DxK array initialiezd with random points
        centroids = points[:, np.random.permutation(N)[:K]]

        # Assigments 1xN array
        labels = np.zeros([1, N])

        for it in np.arange(self.niter):
            # 1. Compute distance to all cluster
                #v1 dirty
            distances = np.zeros([K, N])
            for n in np.arange(N):
                for k in np.arange(K):
                    distances[k, n] = np.sqrt( (points[:, n] - centroids[:, k])**2 ).sum()
            #distances = np.sqrt(((points - centroids[:, np.newaxis, 0])**2)).sum(axis=0)         

            # 2. Update assigments
                # v1 dirty
            for n in np.arange(N):
                kmin = 0
                for k in np.arange(1, K):
                    if distances[k, n] <= distance[kmin, n]:
                        kmin = k
                labels[0, n] = kmin
                # v2 quicker
            #labels = np.argmin(distances, axis=1)

            # 3. Update mean
            for k in np.arange(K):
                centroids[:, k] = np.mean(points[:, labels == k], axis=1)
            #np.array([points[closest==k].mean(axis=0) for k in range(centroids.shape[0])])

        return centroids, label
