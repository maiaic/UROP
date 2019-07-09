import numpy as np
import matplotlib.pylab as plt

srclist_cols = ["row", "ra", "dec", "ra_err", "dec_err", "pos", "x_err", "y_err", "npixsou", "net_counts",\
                "net_counts_err", "bkg_counts", "bkg_counts_err", "net_rate", "net_rate_err", "bkg_rate",\
                "bkg_rate_err", "exptime", "exptime_err", "src_significance", "psf_size", "multi_correl_max",\
                "shape", "radius", "rot_ang", "psfratio", "component"]


class Source():
    """
    A class representing each source found in a given observation
    """
    def __init__(self, ra, dec, ra_err, dec_err, pos, x_err, y_err, npixsou, net_counts, net_counts_err, \
                 bkg_counts, bkg_counts_err, net_rate, net_rate_err, bkg_rate, bkg_rate_err, exptime, \
                 exptime_err, src_significance, psf_size, multi_correl_max, shape, radius, rot_ang, psfratio, \
                 component):
        """
        Parameters:
        """
        self.ra = float(ra)
        self.dec = float(dec)
        self.ra_err = float(ra_err)
        self.dec_err = float(dec_err)
        self.pos = tuple(pos)
        self.x_err = float(x_err)
        self.y_err = float(y_err)
        self.npixsou = int(npixsou)
        self.net_counts = float(net_counts)
        self.net_counts_err = float(net_counts_err)
        self.bkg_counts = float(bkg_counts)
        self.bkg_counts_err = float(bkg_counts_err)
        self.net_rate = float(net_rate)
        self.net_rate_err = float(net_rate_err)
        self.bkg_rate = float(bkg_rate)
        self.bkg_rate_err = float(bkg_rate_err)
        self.exptime = float(exptime)
        self.exptime_err = float(exptime_err)
        self.src_significance = float(src_significance)
        self.psf_size = float(psf_size)
        self.multi_correl_max = int(multi_correl_max)
        self.shape = str(shape)
        self.radius = tuple(radius)
        self.rot_ang = float(rot_ang)
        self.psfratio = float(psfratio)
        self.component = str(component)

        self.toinclude = True

    def get_net_rate(self):
        return self.net_rate


def load_sources_list(filename):
    """
    :Parameters:
    source - obsid_sources.txt as a string

    :return: a dictionary of the point sources
    """
    source_data = open(filename, "r")
    sources = {}

    for line in source_data:
        a_list = line.split()
        if type(a_list[0]) == int:
            sources[a_list[0]] = [i for i in line.split()]

    return sources
