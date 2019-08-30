import numpy as np
import matplotlib.pyplot as plt
import sherpa
import os

sources = os.listdir("obsids/")

def load_data(filename):
    source_data = open(filename, "r")
    src = []
    for line in source_data:
        cat = line.split()

        if "color=magenta" in cat:
            src.append(tuple(cat[0].replace("ellipse","")))

    return src

print(load_data("obsids/18731_reg.txt"))
