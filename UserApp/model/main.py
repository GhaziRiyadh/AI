# from keras import layers, models, optimizers
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from matplotlib import pyplot as plt
from .files import train_cats_dir
from tensorflow import nn, expand_dims
from keras.utils import load_img, img_to_array, array_to_img
from .training import model
from .show import Show, history, train_generator, validation_generator
import numpy as np


def startModels():
    # show data
    Show.show().show()

    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    # use for arg
    # fname = [os.path.join(train_cats_dir, fname)
    #          for fname in os.listdir(train_cats_dir)]

    # imagePath = fname[3]

    # img = image.load_img(imagePath, target_size=(150, 150))

    # x = image.img_to_array(img)
    # x = x.reshape((1,) + x.shape)
    # i = 0
    # for batch in datagen.flow(x, batch_size=1):
    #     plt.figure(i)
    #     imgplot = plt.imshow(image.array_to_img(batch[0]))
    #     i += 1
    #     if i % 4 == 0:
    #         break
    #     plt.show()
