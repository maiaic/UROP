from source_items import Source, load_sources_list

import numpy as np
import matplotlib.pyplot as plt
import os

from sherpa.stats import LeastSq
from sherpa.optmethods import LevMar
from sherpa import data

# Puts all the data in a dictionary indexed by obsid
files = os.listdir("data/")
sources = {}
for filename in files:
    id = filename[:5]
    sources[id] = load_sources_list("data/" + filename)

# Makes a list of all the net rates from the data
rates = []
for obsid in sources.keys():
    for source in sources[obsid]:
        rates.append(source.get_net_rate())

# Make a histogram of NET_RATE => try to fit with gaussian curve to take out outliers + find a good range
rates_array = np.array([i for i in rates if 10 < i < 600])
print(len(rates_array))
(y, edges) = np.histogram(rates_array, "auto")
d2 = data.Data1DInt('gamma', edges[:-1], edges[1:], y)
plt.bar(d2.xlo, d2.y, d2.xhi - d2.xlo)
plt.show()
# This was not super helpful
# Maybe find the mean of the means or something?
