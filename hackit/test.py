from os import listdir
from os.path import isfile,join
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing import image
import matplotlib.pyplot as plt
import csv
from keras import backend as K
import tensorflow as tf
K.clear_session()

graph1 = tf.get_default_graph()

with tf.Session() as sess:
      sess.run(tf.global_variables_initializer())


model = load_model('model5_3_10.h5')
model.compile(loss='mean_squared_error',
               optimizer='Adam',
               metrics=['accuracy'])

# this is tesr

def prediction(id):

    test_dir = 'F:\Github\HackCovid\Dev.ino_HackCovid19\hackit\images'+id+'/'

    onlyfiles = [f for f in listdir(test_dir) if isfile(join(test_dir, f))]
    #
    # print(onlyfiles)
    #

    count = 0
    for files in onlyfiles:
        img = image.load_img(test_dir+files,target_size=(48,48))
        # print(img.shape)
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)

        images = np.vstack([x])
        # plt.imshow(images)
        with graph1.as_default():
            classes = model.predict_classes(images,batch_size=3)


        # print(classes[0])
        arr = ['cough','healthy']

        print(files,classes)


        classes = classes[0]
        if(classes==0):
            count+=1


    return count
