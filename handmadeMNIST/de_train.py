import numpy as np
import matplotlib.pyplot as plt

"""
@:param w = weights
@:param b = bias
@:param i = input
@:h = hidden - скрытый
@:o = output
@:l = label - верный ответ
@: w_i_h - Weights from Input layer to Hidden layer
"""


class CNN:
    def __init__(self, images, labels):
        # Инициализация весов случайными числами
        self.w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
        self.w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
        # Инициализация смещений нулями
        self.b_i_h = np.zeros((20, 1))
        self.b_h_o = np.zeros((10, 1))

        self.learn_rate = 0.2  # шаг обучения
        self.nr_correct = 0  # кол-во правильных предсказаний
        self.epochs = 3  # кол-во итераций обучения
        self.sigmoid = lambda x: 1 / (1 + np.exp(-x))
        self.images, self.labels = images, labels
        self.precision = []

    def fit(self):
        for epoch in range(self.epochs):
            # для расчёта скалярного произведения форматирование в одномерный массив
            for img, lbl in zip(self.images, self.labels):
                img.shape += (1,)
                lbl.shape += (1,)

                # Прямое распр-ие -> Скрытый слой (+ смещение bias)
                h_pre = self.b_i_h + self.w_i_h @ img
                # Ф-я активации
                h = self.sigmoid(h_pre)
                # Скрытый слой -> Вывод (+ смещение bias)
                o_pre = self.b_h_o + self.w_h_o @ h
                # Ф-я активации
                o = self.sigmoid(o_pre)
                # счётчик верных ответов: если макс.ответ слоя вывода == макс.ответу тестовых данных
                self.nr_correct += int(np.argmax(o) == np.argmax(lbl))
                # обратное распр-ие скрытый слой <-- вывод
                delta_o = (2 / len(o)) * (o - lbl)
                # к весу от скрытого слоя до вывода (на каждый нейрон) добавляется произведение
                # его правильности на шаг обучения: у ошибочных показатель отриц. и след-во вычит-ся
                # трансп-ие матриц: согласование матриц
                self.w_h_o += -self.learn_rate * delta_o @ np.transpose(h)
                self.b_h_o += -self.learn_rate * delta_o

                # обратное распр-ие скрытый слой -> ввод
                # (производная композитной ф-ии - производная ф-ии активации, умн-ая на произв-ую ф-ии потерь)
                delta_h = np.transpose(self.w_h_o) @ delta_o * (h * (1 - h))
                self.w_i_h += -self.learn_rate * delta_h @ np.transpose(img)
                self.b_i_h += -self.learn_rate * delta_h

            self.precision.append(round((self.nr_correct / self.images.shape[0]) * 100, 2))
            self.nr_correct = 0

    def test(self):
        for i in self.precision:
            # Точность прогноза для текущий итерации обучения
            print(f"Уверенность: {i}%")

    def predict(self):
        while True:
            index = int(input("Ввод порядкового номера картинки от 1 до 60 000: "))
            img = self.images[index - 1]
            plt.imshow(img.reshape(28, 28), cmap="Greys")

            # прямое распр-ие ввод -> скрытый слой
            h_pre = self.b_i_h + self.w_i_h @ img.reshape(784, 1)
            # Активация сигмода
            h = self.sigmoid(h_pre)
            # Прямое распр-ие скрытый слой -> вывод
            o_pre = self.b_h_o + self.w_h_o @ h
            # Активация сигмоида
            o = self.sigmoid(o_pre)

            # argmax возвращает порядковый номер самого большого элемента в массиве
            plt.title(f"Нейросеть считает, что на картинке цифра {o.argmax()}")
            plt.show()
