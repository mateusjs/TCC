import sys
from sklearn.model_selection import train_test_split
import pandas as pd
import os

for index in range(1, 21):
    for file in os.listdir(sys.argv[1]):
        path = sys.argv[1]
        data_frame = pd.read_csv(sys.argv[1] + file, sep=',')

        column = data_frame.shape[1]
        row = data_frame.shape[0]

        x = data_frame.iloc[0:(row - 1), 0:column - 1]
        y = data_frame.iloc[0:(row - 1), column - 1]

        train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)
        teste = train_x.join(train_y)

        string = str(index)
        teste = teste.reset_index(drop=True)
        teste.to_csv("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\" + string + "\\" + file)