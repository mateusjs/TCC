import pandas as pd
import numpy as np
from pandas2arff import pandas2arff


class Bagging:

    def __init__(self, path, csv_name_final, percentage, n, column):
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column
        self.tamanho = percentage

    def subset(self):
        if self.percentage > 1:
            self.percentage = self.percentage / 100

        # lê o CSV
        data_frame = pd.read_csv(self.csvPath, sep=',')

        for count in range(self.n):
            # Seleciona todos os valores 1 da coluna Class do dataframe e joga para class1, faz o mesmo para o class2
            #  mas com o 2
            df_sub = data_frame.groupby(self.column, as_index=False).apply(
                lambda x: x.sample(frac=self.percentage, replace=True)).reset_index(drop=True)
            new_path = self.csvNameFinal
            subset = str(count)
            value = str(self.tamanho)
            # print("Gerando SubSets")
            # df_sub.to_csv("C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\" + self.csvNameFinal + string + '.csv',
            #               sep=',')
            pandas2arff(df_sub,
                        "C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\bagging\\" + self.csvNameFinal + subset +
                        value + '.arff', cleanstringdata=False)
