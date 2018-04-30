from bagging import Bagging


def main():
    x = Bagging("C:\\Users\\Mateus\\PycharmProjects\\TCC\\Classifiers\\Monk.csv", 'MonkSubSet', 10, 100, 'Class')
    x.subset()

if __name__ == '__main__':
    main()
