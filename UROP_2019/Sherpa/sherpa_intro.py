import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(-5., 5., 200)
ampl_true = 3
pos_true = 1.3
sigma_true = 0.8
err_true = 0.2
y = ampl_true * np.exp(-0.5 * (x - pos_true)**2 / sigma_true**2)
y += np.random.normal(0./ err_true, x.shape)

from sherpa.data import Data1D
d = Data1D("example", x, y)
# print(d)

from sherpa.plot import DataPlot
dplot = DataPlot()
dplot.prepare(d)
dplot.plot()

from sherpa.models.basic import Gauss1D
g = Gauss1D()
print(g)

# from sherpa.plot import ModelPlot
# mplot = ModelPlot()
# mplot.prepare(d,g)
# mplot.plot()