import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import math


class metrica:

    def metrica(path, nome):
        print(type(path))
        data_frame = path

        n = data_frame.shape[1]
        row = data_frame.shape[0]

        x = data_frame.iloc[0:(row - 1), 1:n - 1]
        y = data_frame.iloc[0:(row - 1), n - 1]

        knn = KNeighborsClassifier(n_neighbors=8)
        knn.fit(x, y)
        result = knn.kneighbors(x, return_distance=False)

        aux = []
        for lista in result:
            aux.append(np.delete(lista, 0))

        result = aux
        data_frame2 = data_frame.iloc[:, 0:n - 1]

        # d1 = data_frame.shape[0] / np.prod([max - min for min, max in zip(data_frame2.min(), data_frame2.max())])

        min, max = data_frame2.min(), data_frame2.max()
        min = min.astype('float')
        max = max.astype('float')

        val2 = []
        norma_min, norma_max = float(min.min()), float(max.max())
        norma_n = (data_frame.shape[0] - norma_min) / (norma_max - norma_min)

        for index in range(len(min)):
            max[index] = (max[index] - norma_min) / (norma_max - norma_min)
            min[index] = (min[index] - norma_min) / (norma_max - norma_min)

            val = max[index] - min[index]
            # log = math.log(norma_n / val, 5)
            # print("log:", log)
            # val2.append(log)
            val2.append(norma_n / val)
        auxiliar = 1
        for x in val2:
            auxiliar *= x

        d1 = auxiliar

        volumes = []
        for x in result:
            # print(x)
            instancia = data_frame.iloc[x, 1:n - 1]
            volumes.append(np.prod([max - min for min, max in zip(instancia.min(), instancia.max())]))
        d2 = np.sum(volumes) / data_frame.shape[0]

        sobreposicao = 0
        for index, y in enumerate(result):
            vizinhos = data_frame.iloc[y, -1]
            igual = 0
            n_igual = 0
            nao = 0
            for classe in vizinhos:
                if classe == data_frame.iloc[index, -1]:
                    igual += 1

                else:
                    n_igual += 1
            # print(igual, " ", n_igual)
            if n_igual > igual:
                sobreposicao = sobreposicao + 1
            else:
                nao = nao + 1

        # print(sobreposicao)
        d3 = sobreposicao / data_frame.__len__()
        d2 = str(round(d2, 3))
        d3 = str(round(d3, 3))

        file = open(nome + "metricas", "w")
        file.write(d2 + " " + d3)
        file.close()
        print("D1: ", d1, "D2: ", d2, " D3: ", d3)
