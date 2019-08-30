srclist_cols = ["row", "ra", "dec", "ra_err", "dec_err", "pos", "x_err", "y_err", "npixsou", "net_counts",\
                "net_counts_err", "bkg_counts", "bkg_counts_err", "net_rate", "net_rate_err", "bkg_rate",\
                "bkg_rate_err", "exptime", "exptime_err", "src_significance", "psf_size", "multi_correl_max",\
                "shape", "radius", "rot_ang", "psfratio", "component"]


class Source():
    """
    A class representing each source found in a given observation

    self, ra, dec, ra_err, dec_err, x_pos, y_pos, x_err, y_err, npixsou, net_counts, net_counts_err, \
    bkg_counts, bkg_counts_err, net_rate, net_rate_err, bkg_rate, bkg_rate_err, exptime, \
    exptime_err, src_significance, psf_size, multi_correl_max, shape, r_maj, r_min, rot_ang, psfratio, \
    component
    """
    def __init__(self, param):
        """
        :Parameters:
        param - a list of information about a given source created by load_sources_list
        """
        self.row = param[0]
        self.ra = float(param[1])
        self.dec = float(param[2])
        self.ra_err = float(param[3])
        self.dec_err = float(param[4])
        self.x_pos = float(param[5])
        self.y_pos= float(param[6])
        self.x_err = float(param[7])
        self.y_err = float(param[8])
        self.npixsou = int(param[9])
        self.net_counts = float(param[10])
        self.net_counts_err = float(param[11])
        self.bkg_counts = float(param[12])
        self.bkg_counts_err = float(param[13])
        self.net_rate = float(param[14])
        self.net_rate_err = float(param[15])
        self.bkg_rate = float(param[16])
        self.bkg_rate_err = float(param[17])
        self.exptime = float(param[18])
        self.exptime_err = float(param[19])
        self.src_significance = float(param[20])
        self.psf_size = float(param[21])
        self.multi_correl_max = int(param[22])
        self.shape = str(param[23])
        self.r_maj = float(param[24])
        self.r_min = float(param[25])
        self.rot_ang = float(param[26])
        self.psfratio = float(param[27])
        self.component = str(param[28])

        self.toinclude = True
        self.notes = {}
        self.match = None

    def __str__(self):
        return str("The source at %s, %s") % (self.ra, self.dec)

    def __repr__(self):
        return "Source(%s, %s)" % (self.ra, self.dec)

    def get_net_rate(self):
        return self.net_rate

    def get_shape(self):
        return self.shape

    def get_x(self):
        return self.x_pos

    def get_y(self):
        return self.y_pos

    def get_signif(self):
        return self.src_significance

    def include(self):
        return self.toinclude

    def toggle_toinclude(self):
        self.toinclude = not self.toinclude

    def add_note(self, date, info):
        self.notes[date] = info

    def display_notes(self):
        return self.notes

    def source_match(self, source):
        self.match = source

    def get_match(self):
        return self.match

    def get_row(self):
        return self.row

    def get_x_err(self):
        return self.x_err

    def get_y_err(self):
        return self.y_err

### ----------------------------------------------------------------------------- ###

def load_sources_list(filename):
    """
    :Parameters:
    source - obsid_sources.txt as a string

    :return: a list of the point sources
    """
    sources = []

    with open(filename, "r") as source_data:
        for line in source_data:
            a_list = line.split()
            
            if len(a_list) > 0 and a_list[0].isdigit():
                for place, item in enumerate(a_list):
                    item = item.replace("[", "")
                    item = item.replace("]", "")
                    item = item.replace("(", "")
                    item = item.replace(")", "")
                    item = item.replace(",", "")
                    a_list[place] = item

                sources.append(Source([i for i in a_list if len(i) > 0]))

    return sources

### ----------------------------------------------------------------------- ###

def find_distance(source1, source2):
    """
    :Parameters:
    source1 - a Source object
    source2 - another Source object

    :return:
    a tuple of the  distance between two Source objects and the error in that distance calculation
    """
    x1 = source1.get_x()
    x1_e = source1.get_x_err()

    x2 = source2.get_x()
    x2_e = source2.get_x_err()

    y1 = source1.get_y()
    y1_e = source1.get_y_err()

    y2 = source2.get_y()
    y2_e = source2.get_y_err()

    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    perc_err = ((x2_e + x1_e)*abs(x2 - x1) + (y2_e + y1_e)*abs(y2-y1))/((x2 - x1)**2 + (y2 - y1)**2)
    err = dist * perc_err

    return (dist, err)
