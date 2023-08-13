from keras.preprocessing.image import ImageDataGenerator
from .files import train_dir, validation_dir
from .model import MyModel

model = MyModel()
model = model.generateModels()


def train():
    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )

    validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )

    history = model.fit(
        train_generator,
        steps_per_epoch=100,
        epochs=30,
        validation_data=validation_generator,
        validation_steps=50
    )

    model.save('cats_and_dogs_small_1.h5')

    return history, train_generator, validation_generator
