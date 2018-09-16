import sys
from sklearn.model_selection import train_test_split
import pandas as pd
import os

for file in os.listdir(sys.argv[1]):
    path = sys.argv[1]
    data_frame = pd.read_csv(path + file, sep=',')
    x = data_frame.iloc[:, 0:2].values
    y = data_frame.iloc[:, 2].values
    train_x, aux_x, train_y, aux_y = train_test_split(x, y, test_size=0.5)