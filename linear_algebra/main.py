from scipy import spatial

from Cluster import Centroid
from Vector import Vector
from Matrix import Matrix
from comp_sin import computeSin
import numpy as np


def go_vector():
    v1 = np.array([i for i in range(1, 49, 8)])
    v2 = np.array([i for i in range(-195, -100, 16)])

    vec = Vector(v1, v2)
    print({vec.__str__()})
    vec.print_corr_and_cosine()
    print(f"np.corr: {np.corrcoef(v1, v2)[0, 1]}")
    print(f"SciPy cosine: {spatial.distance.cosine(v1, v2)}")


def go_cluster():
    cen = Centroid()
    # cen.plot_data()
    cen.k_clusters()


def go_matrix():
    m1 = Matrix('M1', 3, 4)
    # print(m1.__str__())
    # print(m1.LU())

    m2 = Matrix('M2', 4, 4)
    # print(m2.__str__())

    numcourses = [13, 4, 12, 3, 14, 13, 12, 9, 11, 7, 13, 11, 9, 2, 5, 7, 10, 0, 9, 7]
    happiness = [70, 25, 54, 21, 80, 68, 84, 62, 57, 40, 60, 64, 45, 38, 51, 52, 58, 21, 75, 70]
    m2.OLS(numcourses, happiness)

    # m.sub_matrix()
    # m.shift_matrix()


def go_sin():
    # градусы
    x = 45
    # погрешность
    n = 0.0000001
    print(str(computeSin(x, n)) + " - синус по ряду Тейлора")


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def count_of_prime(x):
    return f'{(x / np.log(x))}'


def is_prime(q):
    ferma = (np.power(2, (q - 1)) - 1) / q
    return f' Is {q} prime? - {(ferma - int(ferma)) == 0}'


if __name__ == '__main__':
    # go_vector()
    go_cluster()
    # go_matrix()
    # go_sin()
    ex = np.e
    #print('{0:}'.format(ex))
    #print(is_prime(457))