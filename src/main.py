from bagging import Bagging
from plot_data import Data

def main():
    x = Bagging("C:\\Users\\Mateus\\Downloads\\TCC\\classifiers\\Monk.csv", 'MonkSubSet', 10, 100, 'Class')
    x.subset()
    y = Data("C:\\Users\\Mateus\\Downloads\\TCC\\subsets\\MonkSubSet0.csv")
    y.plot()

if __name__ == '__main__':
    main()
