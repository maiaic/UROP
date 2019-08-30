import numpy as np
import matplotlib.pyplot as plt
from sherpa.stats import LeastSq
from sherpa.optmethods import LevMar
from sherpa import data

"""
UNBINNED DATA
"""

np.random.seed(0)
x = np.arange(20, 40, 0.5)
y = x**2 + np.random.normal(0, 10, size=x.size)
d1 = data.Data1D('test', x, y)
# print(d1)

"""
This is the print statement output: 
name      = test
x         = Float64[40]
y         = Float64[40]
staterror = None
syserror  = None

BINNED DATA
"""

z = np.random.gamma(20, scale=0.5, size=1000)
(y, edges) = np.histogram(z)
d2 = data.Data1DInt('gamma', edges[:-1], edges[1:], y)
# print(d2)

"""
This is the print statement output:
name      = gamma
xlo       = Float64[10]
xhi       = Float64[10]
y         = Int64[10]
staterror = None
syserror  = None
"""

# plt.bar(d2.xlo, d2.y, d2.xhi - d2.xlo)

"""
FILTERING DATA
"""

d1.ignore(21.2, 22.8)
d1.x[np.invert(d1.mask)]

from sherpa.models import Polynom1D
from sherpa.fit import Fit
mdl = Polynom1D()
mdl.c2.thaw()
fit = Fit(d1, mdl, stat=LeastSq(), method=LevMar())
res1 = fit.fit()

d1.notice()
res2 = fit.fit()

# print("Degrees of freedom: {} vs {}".format(res1.dof, res2.dof))

"""
VISUALIZING A DATA SET
"""

# from sherpa.plot import DataPlot
# pdata = DataPlot()
# pdata.prepare(d2)
# pdata.plot()
#
# d1.ignore(25, 30)
# d1.notice(26, 27)
# pdata.prepare(d1)
# pdata.plot()

d1.notice()
"""
EVALUATING A MODEL
Use eval_model() and eval_model_to_fit()
"""

d1.notice(22, 25)
y1 = d1.eval_model(mdl)
y2 = d1.eval_model_to_fit(mdl)
x2 = d1.x[d1.mask]
plt.plot(d1.x, d1.y, 'ko', label='Data')
plt.plot(d1.x, y1, '--', label='Model (all points)')
plt.plot(x2, y2, linewidth=2, label='Model (filtered)')
plt.legend(loc=2)
plt.show()

