import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,Activation,MaxPooling2D
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


train_dir = '/home/ekta3501/opensource/Dev.ino_HackCovid19/dataset1/train'

HEIGHT = 48
WIDTH = 48
EPOCHS = 15
BATCH_SIZE = 8
SAMPLE = 27+26
INIT_LR=1e-3

model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=(WIDTH,WIDTH,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


#
# model.add(Conv2D(64,(3,3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(64,(3,3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))
# #
#
# model.add(Conv2D(128, (3,3),border_mode='same',activation='relu'))
# model.add(Conv2D(128, (3,3),border_mode='same',activation='relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.2))
#
# model.add(Dense(256,activation='relu'))
# model.add(Dropout(0.2))


# model.add(Dense(128))
# model.add(Activation('relu'))
# model.add(Dropout(0.2))


model.add(Dense(2))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
   optimizer=Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS),
   metrics=['accuracy'],
   )


train_data_gen = ImageDataGenerator(
       rescale = 1./255,
       shear_range = 0.2,
       zoom_range = 0.2,
       horizontal_flip = True,

)


training_generator = train_data_gen.flow_from_directory(
      train_dir,
      target_size = (WIDTH,HEIGHT),
      batch_size = BATCH_SIZE,
      # class_mode = "categorical",
)

print('train',training_generator.class_indices)

model.fit_generator(
  training_generator,
  steps_per_epoch =SAMPLE // BATCH_SIZE,
  epochs = EPOCHS,
  verbose = 1,
)


model.save('model5_3_10.h5')
