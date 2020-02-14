import numpy as np


def getstationdates(filename):
    """
    Read a single record from IGRA station.
    :param filename: filename of text file to open and read
    :type filename: string
    :return: dates
    :rtype: dataframe
    """

    years = []
    mons = []
    days = []
    hours = []

    lats = []
    lons = []

    lines = open(filename)
    nlines = 0
    for line in lines:
        nlines += 1
        if line[0] == '#':
            toks = line.split()
            years.append(int(toks[1]))
            mons.append(int(toks[2]))
            days.append(int(toks[3]))
            hours.append(int(toks[4]))

            lats.append(float(toks[8]))
            lons.append(float(toks[9]))

        years = np.array(years)
        mons = np.array(mons)
        days = np.array(days)
        hours = np.array(hours)
        lats = np.array(lats) / 10000
        lons = np.array(lons) / 10000

    return years, mons, days, hours, lats, lons
