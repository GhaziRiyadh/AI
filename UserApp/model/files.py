import os
import shutil

# Path to the directory where the original dataset was uncompressed
base_dir = os.path.join('UserApp', 'model')
original_dataset_dir = os.path.join(base_dir, 'dogs-vs-cats')

# Directory where you’ll store your smaller dataset
base_dir = os.path.join(base_dir, 'cats_and_dogs_small')
# os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')  # Original Train directory
# os.mkdir(train_dir)

# Original Validation directory
validation_dir = os.path.join(base_dir, 'validation')
# os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, 'test')  # Original test directory
# os.mkdir(test_dir)

train_cats_dir = os.path.join(train_dir, 'cats')  # Path for training cats
# os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, 'dogs')  # path for training dogs
# os.mkdir(train_dogs_dir)

# Path for validation training cats
validation_cats_dir = os.path.join(validation_dir, 'cats')
# os.mkdir(validation_cats_dir)

# Path for validation training dogs
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
# os.mkdir(validation_dogs_dir)

test_cats_dir = os.path.join(test_dir, 'cats')  # Path for test training cats
# os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, 'dogs')  # Path for test training dogs
# os.mkdir(test_dogs_dir)


# '''Copy the first 1000 cats image for training'''
fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

# '''Copies the next 500 cat images to validation_cats_dir'''
fnames = [f'cat.{i}.jpg' for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src, dst)

# '''Copies the next 500 cat images to test_cats_dir'''
fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src, dst)

# '''Copies the first 1,000 dog images to train_dogs_dir'''
fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src, dst)

# '''Copies the next 500 dog images to validation_dogs_dir'''
fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src, dst)

# '''Copies the next 500 dog images to test_dogs_dir'''
fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, 'train')
    src = os.path.join(src, fname)
    dst = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src, dst)


# test the above code
print('total training cat images:', len(os.listdir(train_cats_dir)))
print('total training dog images:', len(os.listdir(train_dogs_dir)))
print('total validation cat images:', len(os.listdir(validation_cats_dir)))
print('total validation dog images:', len(os.listdir(validation_dogs_dir)))
print('total test cat images:', len(os.listdir(test_cats_dir)))
print('total test dog images:', len(os.listdir(test_dogs_dir)))
