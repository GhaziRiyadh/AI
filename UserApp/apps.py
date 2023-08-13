from django.apps import AppConfig
# from keras.utils import image_dataset_from_directory
# from UserApp.model.files import train_dir,validation_dir
# from tensorflow import data
# from keras import layers, models, losses, Sequential

# batch_size = 32
# img_height = 180
# img_width = 180

# train_ds = image_dataset_from_directory(
#     train_dir,
#     validation_split=0.2,
#     subset="training",
#     seed=123,
#     image_size=(img_height, img_width),
#     batch_size=batch_size)

# val_ds = image_dataset_from_directory(
#     validation_dir,
#     validation_split=0.2,
#     subset="validation",
#     seed=123,
#     image_size=(img_height, img_width),
#     batch_size=batch_size)

# class_names = train_ds.class_names

# AUTOTUNE = data.AUTOTUNE

# train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# normalization_layer = layers.Rescaling(1./255)


class UserappConfig(AppConfig):

    # num_classes = len(class_names)

    # data_augmentation = Sequential(
    #     [
    #         layers.RandomFlip("horizontal", input_shape=(
    #             img_height, img_width, 3)),
    #         layers.RandomRotation(0.1),
    #         layers.RandomZoom(0.1),
    #     ]
    # )

    # model = models.Sequential([
    #     data_augmentation,
    #     layers.Rescaling(1./255),
    #     layers.Conv2D(16, 3, padding='same', activation='relu'),
    #     layers.MaxPooling2D(),
    #     layers.Conv2D(32, 3, padding='same', activation='relu'),
    #     layers.MaxPooling2D(),
    #     layers.Conv2D(64, 3, padding='same', activation='relu'),
    #     layers.MaxPooling2D(),
    #     layers.Dropout(0.2),
    #     layers.Flatten(),
    #     layers.Dense(128, activation='relu'),
    #     layers.Dense(num_classes)
    # ])
    # model.compile(optimizer='adam',
    #               loss=losses.SparseCategoricalCrossentropy(from_logits=True),
    #               metrics=['accuracy'])

    # train
    # epochs = 15
    # history = model.fit(
    #     train_ds,
    #     validation_data=val_ds,
    #     epochs=epochs
    # )
    # model = models.load_model('cats_dogs_1.h5')

    # model.save('cats_dogs_1.h5')

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserApp'
