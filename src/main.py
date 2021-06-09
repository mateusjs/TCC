import os
import sys
import threading

from bagging import Bagging
from boosting import Boosting


def gera_subset(percentage, path, name, index):
    print('Iniciando ', name, ' com porcentagem de ',percentage, ' e repeticao ', index)
    # x = Bagging(path, name, percentage, 100, 'Class', index)
    # x.subset()

    y = Boosting(path, name, percentage, 100, 'Class', index)
    y.subset()


def main():

    percentages = [10, 33, 50, 66]
    threads = []
    for i, files in enumerate(os.listdir(sys.argv[1]), start=1):
        caminho = sys.argv[1] + files

        for file in os.listdir(caminho):
            index = str(i)
            path = sys.argv[1] + index + "\\" + file
            name = file.split('.')[0] + "SubSet"
            for p in percentages:
                threads.append(threading.Thread(
                    target=gera_subset, args=(p, path, name, index)))
                threads[-1].start()

            for t in threads:
                t.join()


if __name__ == '__main__':
    main()
