import matplotlib.pyplot as plt
import numpy as np


class Matrix:
    def __init__(self, name, m_rows, n_cols):
        self.m_rows = m_rows
        self.n_cols = n_cols
        self.name = name
        # self.A = [[3, 4, 5], [9, 12, 15], [0, 1, 2]]
        self.A = np.random.randint(-50, 50, size=(self.m_rows, self.n_cols))

    def __str__(self):
        return f"Matrix {self.name} \n {self.A}"

    def sub_matrix(self):
        sub = self.A[1:4:1, 0:5:1]
        print(f"Sub Matrix: {sub}")

    def shift_matrix(self):
        s = 100
        sh = self.A + s * np.eye(len(self.A))
        print(f"Shift matrix: {sh}")

    def live_evil_matrix(self):
        L = np.random.randint(2, 12, size=(5, 7))
        I = np.random.randint(2, 12, size=(7, 4))
        V = np.random.randint(2, 12, size=(4, 3))
        E = np.random.randint(2, 12, size=(3, 6))

        res1 = (L @ I @ V @ E).T
        res2 = E.T @ V.T @ I.T @ L.T
        print(res1 - res2)

    def inv(self):
        if np.linalg.matrix_rank(self.A) == self.n_cols:
            return f"inv: {np.linalg.inv(self.A)}"
        else:
            return f"pinv: {np.linalg.pinv(self.A)}"

    def q(self):
        Q1 = np.array([[1, -1], [1, 1]]) / np.sqrt(2)
        Q2 = np.array([[1, 2, 2], [2, 1, -2], [-2, 2, -1]]) / 3

        print(Q1.T @ Q1)
        print(Q2.T @ Q2)

    def LU(self):
        import scipy.linalg
        _, L, U = scipy.linalg.lu(self.A)
        print('_ : ', _)
        print('L : ', L)
        print('U : ', U)

    def plot_OLS(self, numcourses, happiness, pred_happiness):
        plt.figure(figsize=(9,9))

        plt.plot(numcourses, happiness, 'ks', markersize = 15)
        plt.plot(numcourses, pred_happiness, 'o-', color = [.6, .6, .6], linewidth = 3, markersize = 15)

        # plot the errors
        for n, y, yHat in zip(numcourses, happiness, pred_happiness):
            plt.plot([n, n], [y, yHat], '--', color =[.8, .8, .8], zorder = -10)

        plt.xlabel('Num of courses taken')
        plt.ylabel('General life happiness')
        plt.xlim([-1, 15])
        plt.ylim([0, 100])
        plt.xticks(range(0, 15, 2))
        plt.legend(['Real data', 'Predicted data', 'Residual'])
        plt.title(f'SSE = {np.sum((pred_happiness - happiness) ** 2):.2f}')
        plt.show()
    def OLS(self, numcourses, happiness):
        X = np.hstack((np.ones((20, 1)), np.array(numcourses, ndmin=2).T))
        print(f'X: \n {X}')
        print(f'X.shape: \n {X.shape}')
        # fit the model using the left-inverse matrix
        X_leftinv = np.linalg.inv(X.T @ X) @ X.T
        print(f'X_leftinv: \n {X_leftinv}')
        beta = X_leftinv @ happiness
        print(f'beta: {beta}')

        # predicted data
        pred_happiness = X @ beta
        print(f'pred_happiness: \n {pred_happiness}')

        self.plot_OLS(numcourses, happiness, pred_happiness)

