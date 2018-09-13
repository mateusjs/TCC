import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from pandas2arff import pandas2arff


class Boosting:

    def __init__(self, path, csv_name_final, percentage, n, column):
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column
        self.tamanho = percentage

    def subset(self):
        data_frame = pd.read_csv(self.csvPath, sep=',')

        if self.percentage > 1:
            self.percentage = self.percentage / 100

        for count in range(self.n):
            df_sub = data_frame.groupby(self.column, as_index=False).apply(
                lambda x: x.sample(frac=self.percentage, replace=True)).reset_index(drop=True)

            n = df_sub.shape[1]
            row = df_sub.shape[0]

            x = df_sub.iloc[0:(row - 1), 1:n - 1]
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
            # salva os subsets em .arff
            pandas2arff(df_sub,
                        "C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\boosting\\" + self.csvNameFinal + subset +
                        value + '.arff', cleanstringdata=False)

        # salva os subsets em .csv
        # df_sub.to_csv(
        #     "C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\boosting\\" + self.csvNameFinal + string + '.csv',
        #     sep=',', index=False)
        # salva os arquivo original após as novas bases em .csv
        # data_frame.to_csv("C:\\Users\\Mateus\\PycharmProjects\\TCC\\newBases\\boosting\\" + self.csvNameFinal + '.csv',
        #                   sep=',', index=False)
        # salva os arquivo original após os erros em .arff
        # pandas2arff(data_frame,
        #             "C:\\Users\\Mateus\\PycharmProjects\\TCC\\arffNewBases\\boosting\\" + self.csvNameFinal + '.arff',
        #             cleanstringdata=False)
