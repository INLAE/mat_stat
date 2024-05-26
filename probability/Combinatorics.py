import math
import numpy as np


class Combinatorics:
    def combinations_rep(self, m, n):
        Cr = math.factorial(n - 1 + m) / (math.factorial(n - 1) * math.factorial(m))
        return Cr

    def combinations(self, m, n):
        C = (math.factorial(n)) / (math.factorial(n - m) * math.factorial(m))
        return C

    def permutations_rep(self, m, n):
        dn = [math.factorial(x) for x in n]
        d = np.prod(dn)
        Pr = math.factorial(n) / math.factorial(d)
        return Pr

    def permutations(self, n):
        P = math.factorial(n)
        return P

    def accomodations_rep(self, m, n):
        Ar = math.pow(n, m)
        return Ar

    def accomodations(self, m, n):
        A = math.factorial(n) / (math.factorial(n - m))
        return A
