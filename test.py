import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate as ip


def interpolateLongitud():
    headers = ['Altura', 'Latitud', 'Longitud']
    data = pd.read_csv("coordenadas.csv", names=headers)
    newLong = []
    newAlt = []
    i = 1000
    while i <= 50000:
        fp = data['Longitud']
        xp = data['Altura']
        y_inter = ip.interp1d(xp, fp)
        newLong.append(y_inter(i))
        newAlt.append(i)
        i += 10
    plt.plot(newLong, newAlt)
    plt.show()


def interpolateLatitud():
    headers = ['Altura', 'Latitud', 'Longitud']
    data = pd.read_csv("coordenadas.csv", names=headers)
    newLat = []
    newAlt = []
    i = 1000
    while i <= 50000:
        fp = data['Latitud']
        xp = data['Altura']
        y_inter = ip.interp1d(xp, fp)
        newLat.append(y_inter(i))
        newAlt.append(i)
        i += 10
    plt.plot(newLat, newAlt)
    plt.show()


if __name__ == '__main__':
    # interpolateLongitud()
    interpolateLatitud()
