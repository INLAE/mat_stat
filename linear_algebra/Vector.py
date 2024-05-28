import numpy as np


class Vector:
    def __init__(self, vector_x, vector_y):
        self.vector_x = vector_x
        self.vector_y = vector_y

    def __str__(self):
        return f"Vec. x: {self.vector_x} " \
               f"Vec. y: {self.vector_y}"

    def corr_and_cosine(self):
        # compute cosine similarity
        num = np.dot(self.vector_x, self.vector_y)
        den = np.linalg.norm(self.vector_x) * np.linalg.norm(self.vector_y)
        cos = num / den

        # compute correlation (similar to above but mean-centered)
        xm = self.vector_x - np.mean(self.vector_x)
        ym = self.vector_y - np.mean(self.vector_x)
        num = np.dot(xm, ym)
        den = np.linalg.norm(xm) * np.linalg.norm(ym)
        cor = num / den

        return cos, cor

    def print_corr_and_cosine(self):
        cor, cos = self.corr_and_cosine()
        print("My correlation: ", cor, "\nMy cosine sim.: ", cos)
