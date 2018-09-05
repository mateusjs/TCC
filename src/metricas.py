import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class metrica_d1:

    def __init__(self, path, csv_name_final, percentage, n, column):
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column

    def metrica(self):
        data_frame = pd.read_csv(self.csvPath)

        n = data_frame.shape[1]
        row = data_frame.shape[0]

        x = data_frame.iloc[0:(row - 1), 1:n - 1]
        y = data_frame.iloc[0:(row - 1), n - 1]


        knn = KNeighborsClassifier(n_neighbors=7)
        knn.fit(x, y)
        result = knn.kneighbors(x, return_distance=False)

        d1 = data_frame.shape[0] / np.prod([max - min for min, max in zip(data_frame.min(), data_frame.max())])

        volumes = []
        for x in result:
            instancia = data_frame.iloc[x, 1:n-1]
            volumes.append(np.prod([max - min for min, max in zip(instancia.min(), instancia.max())]))
        d2 = np.sum(volumes)/data_frame.shape[0]
        

