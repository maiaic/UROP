import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from scipy.optimize import curve_fit
from scipy.stats import chisquare
import math
import actions
import datetime

def linear(x, m, b):
    """
    A linear function
    """
    return m * x + b

def const(x, b):
    """
    Fits a constant
    """
    return 0 * x + b

def rms(y, yfit):
    """
    calculates rms value
    """
    return np.sqrt(np.sum((y-yfit)**2))

"""
:Required things from actions:
    - dates_dict: a dictionary matching obsids to the dates they were taken on
    - to_graph: a dictionary matching intervals to distances in some obsids
"""

def make_a_document(source_pair, x, y, y_err, y_linear, y_null, linear_fit, linear_cov,\
                    null_fit, null_cov):
    """
    Makes a document with the datapoints that were graphed and the statistics stuff
    """
    source1 = source_pair[0]
    source2 = source_pair[1]

    rms_linear = rms(y, y_linear)
    rms_null = rms(y, y_null)

    ddof = len(y) - 1

    chi2_linear = chisquare(y, y_linear, ddof=ddof)

    data_file = open("plots/distance_%s_%s_data.txt" % (source1, source2), "w+")

    data_file.write("Distance between %s and %s\n" % (source1, source2))
    data_file.write("------------------------------------------------\n")

    data_file.write("\n")

    data_file.write("STATISTICS\n")

    data_file.write("\n")

    data_file.write("Linear fit parameters: %s\n" % linear_fit)
    data_file.write("Degrees of freedom: 1\n")
    data_file.write("Linear covariance matrix: \n%s\n" % linear_cov)
    data_file.write("rms error in linear fit: %s\n" % rms_linear)

    data_file.write("\n")

    data_file.write("Null fit parameter: %s\n" % null_fit)
    data_file.write("Null covariance matrix: \n%s\n" % null_cov)
    data_file.write("rms error in null fit: %s\n" % rms_null)

    data_file.write("\n")

    data_file.write("chi-squared test statistic: %s\n" % chi2_linear[0])

    data_file.write("\n")

    data_file.write("------------------------------------------------\n")

    data_file.write("\n")

    data_file.write("DATA\n")

    data_file.write("## DATE    OBSID   DISTANCE    ERROR\n")

    for i in range(len(x)):
        iso_date = datetime.date.isoformat(dates.num2date(x[i]))
        obsid = actions.reverse_dates_dict()[iso_date]
        distance = y[i]
        error = y_err[i]

        data_file.write("%s %s    %s   %s    %s\n" % (i, iso_date, obsid, distance, error))

    data_file.close()

def graph_distances(source_pair, start_date="1999-01-01", end_date="2020-01-01"):
    """
    A function that creates a graph

    :parameters:
        source_pair - a tuple of the pair of sources
        start_date - an int of the year you want to start graphing at (def = 1999-01-01)
        end_date - an int of the year you want to stop graphing at (def = 2020-01-01)

    :output:
    A PNG file with a graph of the distances between the desired sources
    A TXT file with the data points and some statistics
    """
    start = dates.datestr2num(start_date)
    end = dates.datestr2num(end_date)
    to_graph = actions.to_graph()
    dates_dict = actions.dates_dict()

    try:
        data = to_graph[source_pair]
    except :
        source_pair = (source_pair[1], source_pair[0])
        data = to_graph[source_pair]
    x = []
    y = []
    err = []

    for instance in data:
        obsid = instance[0]
        if obsid in dates_dict.keys():
            distance = instance[1][0]
            error = instance[1][1]

            date_num = dates.datestr2num(dates_dict[obsid])

            if start <= date_num <= end:
                    x.append(date_num)
                    y.append(distance)
                    err.append(error)

    x = np.array(x)
    y = np.array(y)
    err = np.array(err)

    popt_linear, pcov_linear = curve_fit(linear, x, y, sigma=err)
    popt_const, pcov_const = curve_fit(const, x, y, sigma=err)

    yfit_linear = linear(x, popt_linear[0], popt_linear[1])
    yfit_const = const(x, popt_const[0])

    fig, ax = plt.subplots()

    make_a_document(source_pair, x, y, err, yfit_linear, yfit_const, popt_linear,\
                    pcov_linear, popt_const, pcov_const)

    ax.set(xlabel="Observation date", ylabel="Distance between sources")
    ax.set_title("%s Distance by Function of Time" % str(source_pair))
    ax.errorbar(x, y, yerr=err, fmt="o", label="Data")
    ax.plot(x, yfit_linear, "r", label="Line of Best Fit")
    ax.plot(x, yfit_const, "g", label="null")
    ax.legend()

    fig.savefig("plots/distance_%s_%s_all" % (source_pair[0], source_pair[1]))

    plt.close(fig)
