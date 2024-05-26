import numpy as np
from scipy.integrate import quad
from Combinatorics import Combinatorics as comb


class Bernoulli:
    def bernoulli_formula(self, m, n, p):
        p = comb.combinations(m, n) * np.power(p, m) * np.power(1 - p, n - m)
        return p

    def deMoivre_Laplace_theorem(self, n, m, p, q):
        x = (m - n * p) / np.sqrt(n * p * q)
        fx = (1 / np.sqrt(2 * np.pi)) * np.power(np.e, (-(x ** 2 / 2)))
        P = fx / np.sqrt(n * p * q)
        return P

    def integral_theorem_deMoivre_Laplace(self, a, b, n, p):
        q = 1 - p
        x1 = (a - n * p) / np.sqrt(n * p * q)
        x2 = (b - n * p) / np.sqrt(n * p * q)
        print(f'x1 = {x1} \nx2 = {x2}')
        f = lambda t: np.e ** (-(t ** 2 / 2))
        C = 2 / (np.sqrt(2 * np.pi))
        F1 = C * (quad(f, 0, x1)[0])
        F2 = C * (quad(f, 0, x2)[0])
        print(f'F1 = {F1} \nF2 = {F2}')
        P = 1 / 2 * (F2 - F1)
        return P
