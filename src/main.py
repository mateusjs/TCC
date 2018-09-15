from bagging import Bagging
from boosting import Boosting
from metricas import metrica_d1
from dcol import Dcol
import sys
import os
import threading


def gera_subset(percentage, path, name):
    print('Iniciando ', name, 'com porcentagem de ', percentage)
    x = Bagging(path, name, percentage, 100,
                'Class')
    x.subset()

    # y = Boosting(path, name, percentage, 100,
    #              'Class')
    # y.subset()

    k = metrica_d1(path, name, percentage, 1,
                   'Class')
    k.metrica()


def main():
    percentages = [10, 33, 50, 60]
    threads = []

    for file in os.listdir(sys.argv[1]):
        path = sys.argv[1] + "\\" + file
        name = file.split('.')[0] + "SubSet"

        for p in percentages:
            threads.append(threading.Thread(target=gera_subset, args=(p, path, name)))
            threads[-1].start()

        for t in threads:
            t.join()


if __name__ == '__main__':
    main()
