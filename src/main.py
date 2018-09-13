from bagging import Bagging
from boosting import Boosting
from metricas import metrica_d1
from dcol import Dcol


def main():
    percentages = [10, 33, 50, 66]
    name = "C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Banana.csv"
    name = name.split("\\")
    name = name[name.__len__()-1]
    name = name.split('.')[0]+"SubSet"


    for percentage in percentages:

        x = Bagging("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Banana.csv", name, percentage, 100, 'Class')
        x.subset()
        y = Boosting("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Banana.csv", name, percentage, 100, 'Class')
        y.subset()

        # file_object = open("C:\\Users\\Mateus\\PycharmProjects\\TCC\\subsets\\MonkSubSet.bat", "w")
        #
        # for count in range(0, 100):
        #     string = str(count)
        #     file_object.write("csv2arff MonkSubSet" + string + ".csv ", name + string + ".arff\n")
        #
        # file_object.close()

        # z = Dcol()
        # z.DcolI()

        k = metrica_d1("C:\\Users\\Mateus\\PycharmProjects\\TCC\\classifiers\\Banana.csv", name, percentage, 1, 'Class')
        k.metrica()


if __name__ == '__main__':
    main()
