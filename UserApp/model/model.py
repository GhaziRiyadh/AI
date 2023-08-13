from keras import layers, models, optimizers


class MyModel:
    def __init__(self) -> None:
        self._model = models.Sequential()

    def generateModels(self):
        self._model.add(layers.Conv2D(
            32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self._model.add(layers.MaxPooling2D((2, 2)))
        self._model.add(layers.Flatten())
        self._model.add(layers.Dense(512, activation='relu'))
        self._model.add(layers.Dense(1, activation='sigmoid'))
        self._model.compile(
            loss='binary_crossentropy',
            optimizer=optimizers.RMSprop(lr=1e-4),
            metrics=['acc']
        )

        return self._model
