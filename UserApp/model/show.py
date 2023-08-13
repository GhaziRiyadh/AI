import matplotlib.pyplot as plt
from .training import train

history, train_generator, validation_generator = train()


class Show:
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)

    def show(self):
        plt.plot(self.epochs, self.acc, 'bo', label='Training acc')
        plt.plot(self.epochs, self.val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()
        plt.figure()
        plt.plot(self.epochs, self.loss, 'bo', label='Training loss')
        plt.plot(self.epochs, self.val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend()

        return plt
