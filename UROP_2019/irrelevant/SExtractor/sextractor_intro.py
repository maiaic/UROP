import numpy as np
import sep
import fitsio
import matplotlib.pyplot as plt
from matplotlib import rcParams

data = fitsio.read("/sgrastar/maiac/sgrastar/data/3392/repro/acisf03392_repro_evt2.fits")

m = np.mean(data)
s = np.std(data)
plt.imshow(data, interpolation='nearest', cmap='gray', vmin=m-s, vmax=m+s, origin='lower')
plt.colorbar()