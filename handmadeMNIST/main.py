from data import mnist
from de_train import CNN


def recognize_mnist():
    # экз. класса обработки датасета
    data = mnist()
    images, labels = data.get_mnist()
    # экз. класса модели маш.обучения
    cnn = CNN(images, labels)
    cnn.fit()
    cnn.test()
    cnn.predict()


if __name__ == '__main__':
    recognize_mnist()
