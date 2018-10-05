import pandas as pd
from src.pandas2arff import pandas2arff
from src.dcol import Dcol
from src.metricas import metrica


class Bagging:

    def __init__(self, path, csv_name_final, percentage, n, column, repeticao):
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column
        self.tamanho = percentage
        self.repeticao = repeticao

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
            subset = str(count)
            value = str(self.tamanho)
            caminho = str(self.repeticao)
            # df_sub.to_csv( "C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\bagging\\" + self.csvNameFinal + subset + "_" + value, sep=',')
            pandas2arff(df_sub,
                        "C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\bagging\\" + self.csvNameFinal + subset +
                        "_" + value + '.arff', cleanstringdata=False)
            Dcol.DcolI("C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\bagging\\", self.csvNameFinal + subset +
                       "_" + value + '.arff', self.csvNameFinal + subset + "_" + value)

            metrica.metrica(df_sub, "C:\\Users\\Mateus\\Documents\\TCC\\"+caminho+"\\bagging\\" + self.csvNameFinal +
                            subset + "_" + value + ".txt")
