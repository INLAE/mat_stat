from Combinatorics import Combinatorics
import numpy as np
from matplotlib import pyplot as plt
from Bernulli_test import Bernoulli

def classical_probability(fit, all):
    return fit / all

# "Парадкос" дней рождения укладывается
# в отношение перестановок без повторений и с ними
def birth_paradox(comb):
    n_people = 40
    days = 365
    fav = comb.accomodations(n_people, days)
    all = comb.accomodations_rep(n_people, days)
    print(f"Вероятность совпадения дня рождения "
          f"хотя бы у одной пары людей из {n_people} "
          f"человек равна {1 - round(classical_probability(fav, all), 2)}")


if __name__ == '__main__':
    comb = Combinatorics()
    bern = Bernoulli()
    print(bern.deMoivre_Laplace_theorem(400, 180, 0.5, 0.5))
    birth_paradox(comb)