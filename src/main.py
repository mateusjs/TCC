from bagging import Bagging
from boosting import Boosting
from metricas import metrica_d1
from dcol import Dcol


def main():
    x = Bagging("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Monk.csv", 'MonkSubSet', 10, 1, 'Class')
    x.subset()
    y = Boosting("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Monk.csv", 'MonkSubSet', 10, 50, 'Class')
    y.subset()

    # file_object = open("C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\MonkSubSet.bat", "w")
    #
    # for count in range(0, 100):
    #     string = str(count)
    #     file_object.write("csv2arff MonkSubSet" + string + ".csv MonkSubSet" + string + ".arff\n")
    #
    # file_object.close()

    # z = Dcol()
    # z.DcolI()

    k = metrica_d1("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Banana.csv", 'MonkSubSet', 10, 1, 'Class')
    k.metrica()


if __name__ == '__main__':
    main()
