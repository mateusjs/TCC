import pandas as pd



class Bagging:

    def __init__(self, path, csv_name_final, percentage, n, column):
        print(self)
        self.csvPath = path
        self.csvNameFinal = csv_name_final
        self.percentage = percentage
        self.n = n
        self.column = column

    def subset(self):
        if self.percentage > 1:
            self.percentage = self.percentage / 100

        #lê o CSV
        dataFrame = pd.read_csv(self.csvPath, sep=',')

        #Seleciona todos os valores 1 da coluna Class do dataframe e joga para class1, faz o mesmo para o class2 mas com o 2
        dfSub = dataFrame.groupby(self.column, as_index=False).apply(lambda x: x.sample(frac=self.percentage)).reset_index(drop=True)

        for count in range(self.n):
            new_path = self.csvNameFinal
            string = str(count)
            print("Gerando SubSets")
            dfSub.to_csv("C:\\Users\\Mateus\\Downloads\\TCC\\subsets\\" + self.csvNameFinal + string + '.csv', sep=',')

