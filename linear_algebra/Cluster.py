import numpy as np
from matplotlib import pyplot as plt


class Centroid:
    def __init__(self):
        self.n = 50
        self.blur = 1
        self.A = [1, 1]
        self.B = [-3, 1]
        self.C = [3, 3]

        a = [self.A[0] + np.random.randn(self.n) * self.blur,
             self.A[1] + np.random.randn(self.n) * self.blur]
        b = [self.B[0] + np.random.randn(self.n) * self.blur,
             self.B[1] + np.random.randn(self.n) * self.blur]
        c = [self.C[0] + np.random.randn(self.n) * self.blur,
             self.C[1] + np.random.randn(self.n) * self.blur]

        self.data = np.transpose(np.concatenate((a, b, c), axis=1))

    def plot_data(self):
        plt.plot(self.data[:, 0], self.data[:, 1], 'ko', markerfacecolor='w')
        plt.title('Raw (preclustered) data')
        plt.xticks([])
        plt.yticks([])

        plt.show()

    def k_clusters(self):
        k = 3
        ridx = np.random.choice(range(len(self.data)), k, replace=False)
        centroids = self.data[ridx, :]

        # setup the figure
        fig, axs = plt.subplots(2, 2, figsize=(6, 6))
        axs = axs.flatten()
        lineColors = [[0, 0, 0], [.4, .4, .4], [.8, .8, .8]]

        # plot data with initial random cluster centroids
        axs[0].plot(self.data[:, 0], self.data[:, 1], 'ko', markerfacecolor='w')
        axs[0].plot(centroids[:, 0], centroids[:, 1], 'ko')
        axs[0].set_title('Iteration 0')
        axs[0].set_xticks([])
        axs[0].set_yticks([])

        # loop over iterations
        for i in range(3):
            # step 1: compute distance
            distance = np.zeros((self.data.shape[0], k))
            for c in range(k):
                distance[:, c] = np.sum((self.data - centroids[c, :]) ** 2, axis=1)

            # step 2: assign to group based on minimum distance
            groupidx = np.argmin(distance, axis=1)

            # step 3: recompute centers
            for ki in range(k):
                centroids[ki, :] = [np.mean(self.data[groupidx == ki, 0]),
                                    np.mean(self.data[groupidx == ki, 1])]

            # plot data points
            for j in range(len(self.data)):
                axs[i + 1].plot([self.data[j, 0], centroids[groupidx[j], 0]],
                                [self.data[j, 1], centroids[groupidx[j], 1]], color=lineColors[groupidx[j]])

                axs[i + 1].plot(centroids[:, 0], centroids[:, 1], 'ko')
                axs[i + 1].set_title(f'Iteration {i + 1}')
                axs[i + 1].set_xticks([])
                axs[i + 1].set_yticks([])
        self.plot_data()
        plt.show()
