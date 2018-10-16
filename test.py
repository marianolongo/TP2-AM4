import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def test():
    headers = ['Altura', 'Latitud', 'Longitud']
    data = pd.read_csv("coordenadas.csv", names=headers)
    # aux = list()
    # for i in data['Altura']:
    #     hello = np.interp(i, data["Latitud"], data['Altura'])
    #     aux.append(hello)
    # print(aux)
    aux = list()
    for i in data['Altura']:
        aux.append(data['Altura'].get(i))
    print("hello")
    asd = np.interp(1000000, data['Altura'], data['Latitud'])
    print(asd)
    # plt.plot(data['Latitud'], data['Altura'])
    # plt.show()


if __name__ == '__main__':
    test()