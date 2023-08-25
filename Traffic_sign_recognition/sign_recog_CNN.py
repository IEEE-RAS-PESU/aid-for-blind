import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam
import tensorflow as tf
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pickle
import os
import pandas as pd
import random
from keras.preprocessing.image import ImageDataGenerator

data_path = "myData"
label_file = 'labels.csv'
batch_size_value = 50
steps_per_epoch_value = 2000
epochs_value = 10
image_dimensions = (32, 32, 3)
test_ratio = 0.2
validation_ratio = 0.2

count = 0
images = []
class_numbers = []
class_list = os.listdir(data_path)
print("Total Classes Detected:", len(class_list))
num_classes = len(class_list)
print("Importing Classes.....")
for class_index in range(0, len(class_list)):
    class_images_list = os.listdir(data_path + "/" + str(count))
    for img_name in class_images_list:
        cur_img = cv2.imread(data_path + "/" + str(count) + "/" + img_name)
        images.append(cur_img)
        class_numbers.append(count)
    print(count, end=" ")
    count += 1
print(" ")
images = np.array(images)
class_numbers = np.array(class_numbers)

X_train, X_test, y_train, y_test = train_test_split(images, class_numbers, test_size=test_ratio)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_ratio)

data = pd.read_csv(label_file)
print("data shape ", data.shape, type(data))

def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

X_train = np.array(list(map(preprocessing, X_train)))
X_validation = np.array(list(map(preprocessing, X_validation)))
X_test = np.array(list(map(preprocessing, X_test)))
cv2.imshow("GrayScale Images", X_train[random.randint(0, len(X_train) - 1)])

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
X_validation = X_validation.reshape(X_validation.shape[0], X_validation.shape[1], X_validation.shape[2], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)

data_gen = ImageDataGenerator(width_shift_range=0.1,
                              height_shift_range=0.1,
                              zoom_range=0.2,
                              shear_range=0.1,
                              rotation_range=10)

data_gen.fit(X_train)
batches = data_gen.flow(X_train, y_train, batch_size=20)

X_batch, y_batch = next(batches)

y_train = to_categorical(y_train, num_classes)
y_validation = to_categorical(y_validation, num_classes)
y_test = to_categorical(y_test, num_classes)

def create_model():
    num_filters = 60
    filter_size = (5, 5)
    filter_size2 = (3, 3)
    pool_size = (2, 2)
    num_nodes = 500
    model = Sequential()
    model.add(Conv2D(num_filters, filter_size, input_shape=(image_dimensions[0], image_dimensions[1], 1), activation='relu'))
    model.add(Conv2D(num_filters, filter_size, activation='relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Conv2D(num_filters // 2, filter_size2, activation='relu'))
    model.add(Conv2D(num_filters // 2, filter_size2, activation='relu'))
    model.add(MaxPooling2D(pool_size=pool_size))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(num_nodes, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

trained_model = create_model()
print(trained_model.summary())
history = trained_model.fit_generator(data_gen.flow(X_train, y_train, batch_size=batch_size_value),
                                      steps_per_epoch=steps_per_epoch_value,
                                      epochs=epochs_value,
                                      validation_data=(X_validation, y_validation),
                                      shuffle=1)

pickle_out = open("model_trained.p", "wb")
pickle.dump(trained_model, pickle_out)
pickle_out.close()
cv2.waitKey(0)
