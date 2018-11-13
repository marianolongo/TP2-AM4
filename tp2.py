import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import interpolate as ip
from mpl_toolkits.mplot3d import Axes3D


def interpolate_longitude(aux):
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
        i += aux
    return newLong


def interpolate_latitude(aux):
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
        i += aux
    # plt.plot(newLat, newAlt)
    # plt.show()
    return newLat


def extrapolate_latitude(aux):
    headers = ['Altura', 'Latitud', 'Longitud']
    data = pd.read_csv("coordenadas.csv", names=headers)
    newLat = []
    newAlt = []
    i = 0
    while i <= 1000:
        fp = data['Latitud']
        xp = data['Altura']
        y_inter = ip.interp1d(xp, fp, fill_value="extrapolate")
        newLat.append(y_inter(i))
        newAlt.append(i)
        i += aux
    return newLat


def extrapolate_longitude(aux):
    headers = ['Altura', 'Latitud', 'Longitud']
    data = pd.read_csv("coordenadas.csv", names=headers)
    newLong = []
    newAlt = []
    i = 0
    while i <= 1000:
        fp = data['Longitud']
        xp = data['Altura']
        y_inter = ip.interp1d(xp, fp, fill_value="extrapolate")
        newLong.append(y_inter(i))
        newAlt.append(i)
        i += aux
    return newLong


def create_new_coordenadas_csv(aux):
    """
    Funcion utilizada para crear las coordenadas interpoladas cada 10km.
    :param aux: Utilizado para interpolar cada 10km o 1km.
    """
    new_interpolated_latitudes = interpolate_latitude(aux)
    new_interpolated_longitudes = interpolate_longitude(aux)
    new_extrapolated_longitudes = extrapolate_longitude(aux)
    new_extrapolated_latitudes = extrapolate_latitude(aux)

    with open('coordenadas_interpoladas' + str(aux), 'w+') as f:
        print("Altura,Latitud,Longitud", file=f)
        altura = 50000
        i = new_interpolated_latitudes.__len__() - 1
        while altura >= 1000:
            print(str(altura))
            print(str(altura) + "," + str(new_interpolated_latitudes[i]) + "," + str(new_interpolated_longitudes[i]),
                  file=f)
            altura -= aux
            i -= 1
        i = new_extrapolated_latitudes.__len__() - 1
        while altura >= 0:
            print(str(altura))
            print(str(altura) + "," + str(new_extrapolated_latitudes[i]) + "," + str(new_extrapolated_longitudes[i]),
                  file=f)
            altura -= aux
            i -= 1


def plot_3d():
    """
    Funcion utilizada para realizar el grafico 3d.
    """
    csv = pd.read_csv("coordenadas_interpoladas10")
    x = csv["Latitud"]
    y = csv["Longitud"]
    z = csv["Altura"]

    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x, y, z)
    ax.legend()
    plt.xlabel("Latitud")
    plt.ylabel("Longitud")

    plt.show()


def plot_2d(aux):
    """
    Este metodo es el utilizado para crear los graficos 2d.
    :param aux: Utilizado para pasarle Longitud y Latitud
    """
    csv = pd.read_csv("coordenadas_interpoladas10")
    alturas = csv["Altura"]
    datos = csv[aux]
    plt.plot(datos.values, alturas.values)
    plt.ylabel("Altura")
    plt.xlabel(aux)
    plt.show()


if __name__ == '__main__':
    create_new_coordenadas_csv(10)
    create_new_coordenadas_csv(1)
    plot_3d()
    plot_2d("Longitud")
    plot_2d("Latitud")
