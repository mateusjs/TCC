import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from src.pandas2arff import pandas2arff
from src.dcol import Dcol
from src.metricas import metrica


class Boosting:

    def __init__(self, path, csv_name_final, percentage, n, column, repeticao):
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column
        self.tamanho = percentage
        self.repeticao = repeticao

    def subset(self):
        data_frame = pd.read_csv(self.csvPath, sep=',')

        if self.percentage > 1:
            self.percentage = self.percentage / 100

        for count in range(self.n):
            df_sub = data_frame.groupby(self.column, as_index=False).apply(
                lambda x: x.sample(frac=self.percentage, replace=True)).reset_index(drop=True)

            n = df_sub.shape[1]
            row = df_sub.shape[0]

            x = df_sub.iloc[0:(row - 1), 0:n - 1]
            y = df_sub.iloc[0:(row - 1), n - 1]

            knn = KNeighborsClassifier(n_neighbors=3)
            knn.fit(x, y)
            result = knn.predict(x)

            for it in range(0, row - 1):
                if y[it] != result[it]:
                    data_frame = data_frame.append([df_sub.iloc[it, :]], ignore_index=True)

                self.percentage = (df_sub.shape[0] / data_frame.shape[0])

            subset = str(count)
            value = str(self.tamanho)
            caminho = str(self.repeticao)
            # salva os subsets em .arff
            pandas2arff(df_sub,
                        "C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\boosting\\" + self.csvNameFinal + subset +
                       "_" + value + '.arff', cleanstringdata=False)
            Dcol.DcolI("C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\boosting\\", self.csvNameFinal + subset +
                       "_" + value + '.arff', self.csvNameFinal + subset + "_" + value)
            metrica.metrica(df_sub,
                            "C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\boosting\\" + self.csvNameFinal + subset + "_" + value + ".txt")