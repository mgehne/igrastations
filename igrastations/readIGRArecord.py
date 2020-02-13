import pandas as pd
import numpy as np


def readIGRArecord(filename, date, levtyp='all'):
    """
    Read a single record from IGRA station.
    :param filename: filename of text file to open and read
    :type filename: string
    :param date: date to be read, format is yyyymmddhh
    :type date: string
    :param levtyp: 'pres' or 'all', read all levels or only pressure levels
    :type levtyp: string
    :return: dataout
    :rtype: dataframe
    """
    vars = ['lvltyp', 'etime', 'pres', 'gph', 'temp', 'rh', 'dpdp', 'wdir', 'wspd']
    istrt = [2, 5, 11, 18, 24, 30, 36, 42, 48]
    ilast = [4, 10, 17, 23, 29, 35, 41, 47, 53]
    nvar = len(vars)

    lines = open(filename)
    nlines = 0
    for line in lines:
        nlines += 1
        if line[0] == '#':
            toks = line.split()
            currdate = toks[1] + toks[2] + toks[3] + toks[4]
            if currdate == date:
                print('date is in record')
                nlev = int(toks[6]) - 1
                dat = pd.read_table(filename, skiprows=nlines, nrows=nlev, names=vars)
                break

    datv = dat.values
    data = np.empty([nlev, nvar])
    ll = 0
    for line in datv:
        for ii in np.arange(0, nvar):
            strtmp = str(line)[istrt[ii]:ilast[ii]]
            data[ll, ii] = int(strtmp)
        ll += 1

    if levtyp == 'pres':
        ilevp = np.where((data[:, 0] == 10) | (data[:, 0] == 21))
        dataout = pd.DataFrame(data[ilevp], columns=vars)
    else:
        dataout = pd.DataFrame(data, columns=vars)

    return dataout
