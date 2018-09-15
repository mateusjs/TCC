import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split
import scipy

for file in os.listdir(sys.argv[1]):
    data_frame = pd.read_csv(sys.argv[1] + file, sep=',')
    train, test = train_test_split(data_frame, test_size=0.5)
    train.to_csv("C:\\Users\\Mateus\\Documents\\classificadores\\"+file)