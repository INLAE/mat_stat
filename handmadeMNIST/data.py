import pathlib
import numpy as np

''' x_train содержит изображения цифр
        y_train содержит метки цифр (от 0 до 9)
        :return images, labels:  '''


class mnist:
    def load_data(self):
        with np.load(f"{pathlib.Path(__file__).parent.absolute()}/data/mnist.npz") as f:
            images, labels = f["x_train"], f["y_train"]
        return images, labels

    def get_mnist(self):
        images, labels = self.load_data()
        # оцифровка изображений и апроксимация в диапазон (0; 1)
        images = images.astype("float32") / 255
        # двумерный массив images[a, b],
        # где a - кол-во картинок цифры, b - кол-во пикселей всех картинок цифры (длина х ширина)
        images = np.reshape(images, (images.shape[0], images.shape[1] * images.shape[2]))
        # one hot encoding
        # нулевая матрица, где индекс значения в строке = 1 согласно меткам цифр y_train
        labels = np.eye(10)[labels]
        return images, labels
