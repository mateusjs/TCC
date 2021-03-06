import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import math


class metrica:

    def metrica(path, nome):

        data_frame = path

        df_aux = data_frame.groupby(['Class']).size().to_frame()
        df_aux = df_aux * 1.0

        column = data_frame.shape[1]
        row = data_frame.shape[0]

        for coluna in df_aux:
            df_aux[coluna] = df_aux[coluna] / row

        x = data_frame.iloc[0:(row - 1), 1:column - 1]
        y = data_frame.iloc[0:(row - 1), column - 1]

        knn = KNeighborsClassifier(n_neighbors=8)
        knn.fit(x, y)
        result = knn.kneighbors(x, return_distance=False)

        aux = []
        for lista in result:
            aux.append(np.delete(lista, 0))

        result = aux
        data_frame2 = data_frame.iloc[:, 0:column - 1]

        # d1 = data_frame.shape[0] / np.prod([max - min for min, max in zip(data_frame2.min(), data_frame2.max())])

        # min, max = data_frame2.min(), data_frame2.max()
        # min = min.astype('float')
        # max = max.astype('float')
        #
        # val2 = []
        # norma_min, norma_max = float(min.min()), float(max.max())
        # norma_n = (data_frame.shape[0] - norma_min) / (norma_max - norma_min)

        # for index in range(len(min)):
        #     max[index] = (max[index] - norma_min) / (norma_max - norma_min)
        #     min[index] = (min[index] - norma_min) / (norma_max - norma_min)
        #
        #     val = max[index] - min[index]
        #     # log = math.log(norma_n / val, 5)
        #     # print("log:", log)
        #     # val2.append(log)
        #     val2.append(norma_n / val)
        # auxiliar = 1
        # for x in val2:
        #     auxiliar *= x
        #
        # d1 = auxiliar

        volumes = []
        for x in result:
            # print(x)
            instancia = data_frame.iloc[x, 1:column - 1]
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

        df_sub = pd.read_fwf(nome, header=None, sep=' ')

        df_sub = df_sub.iloc[:, 1:df_sub.shape[1]]

        if df_aux.shape[0] > 2:
            df_sub = df_sub.mul(pd.Series(df_aux.iloc[:, 0].values), axis=0)

        teste = df_sub.sum(axis=0, numeric_only=True)
        teste = teste.append(pd.Series([d3]))

        df = teste.to_frame()
        df.to_csv(nome, index=False, sep=' ', header=None, float_format='%.3f')
