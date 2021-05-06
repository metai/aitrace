
import numpy as np
from skpp import ProjectionPursuitRegressor
estimator = ProjectionPursuitRegressor()
estimator.fit(np.arange(10).reshape(10, 1), np.arange(10))


