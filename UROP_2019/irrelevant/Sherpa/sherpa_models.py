import numpy as np
import matplotlib.pyplot as plt
from sherpa import models

"""
CREATING A MODEL INSTANCE
"""
g = models.Gauss1D()
print(g)

"""
COMBINING MODELS
"""

src1 = models.Gauss1D('scr1')
back = models.Const1D('back')
mdl1 = src1 + back
print(mdl1)

src2 = models.Gauss1D('src2')
mdl2 = src2 + 2 * back
print(mdl2)
