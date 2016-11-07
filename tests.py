import pytest
import numpy as np

from algoClean import *


def testKHigherThanN():
	kmean = KMeanClean()
	points = np.zeros([2, 5])

	with pytest.raises(KmeanExceptDHigherThanN):
		kmean.run(points, 20)