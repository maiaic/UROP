import numpy as np
import matplotlib.pyplot as plt
from sherpa.stats import LeastSq
from sherpa.optmethods import LevMar
from sherpa import data

z = np.random.gamma(20, scale=0.5, size=1000)
print(z)
print(len(z))
(y, edges) = np.histogram(z)
d2 = data.Data1DInt('gamma', edges[:-1], edges[1:], y)
print(d2)
plt.bar(d2.xlo, d2.y, d2.xhi - d2.xlo)
plt.show()
