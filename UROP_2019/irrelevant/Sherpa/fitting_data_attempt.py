import numpy as np
import matplotlib.pyplot as plt
from sherpa.stats import LeastSq
from sherpa.optmethods import LevMar
from sherpa.models import Polynom1D
from sherpa.fit import Fit
from sherpa.plot import DataPlot, ModelPlot
from sherpa import data

# distances = open("distances.txt", "r")
mdl = Polynom1D()
mdl.c2.thaw()
print(mdl)

# Establishes what the data set is and prepares it to be plotted
x = np.arange(2002, 2009)
y = np.array([float(i) for i in distances])
d1 = data.Data1D('distances', x, y)

# pdata = DataPlot()
# pdata.prepare(d1)
#
# mplot = ModelPlot()
# mplot.prepare(d1, mdl)
#
# pdata.plot()
# mplot.plot(overplot=True)

y1 = d1.eval_model(mdl)
print(y1)

plt.plot(d1.x, d1.y, "ko", label="Data")
plt.plot(d1.x, y1, linewidth=2, label="Model")
plt.legend(loc=2)
plt.show()

