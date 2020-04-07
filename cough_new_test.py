from os import listdir
from os.path import join,isfile
from keras.preprocessing import image
from keras.models import load_model
import time
import tensorflow as tf
from keras import backend as K
import tensorflow as tf
import numpy as np
# K.clear_session()

model = load_model("model1_new_5_6.h5")
# model._make_predict_function()
graph1 = tf.get_default_graph()

# with tf.Session() as sess:
#       sess.run(tf.global_variables_initializer())




test_dir = '/home/ekta3501/opensource/Dev.ino_HackCovid19/dataset/train/healthy/'

model.compile(loss="categorical_crossentropy",
            optimizer='adam',
            metrics=['accuracy']
)

onlyfiles = [f for f in listdir(test_dir) if isfile(join(test_dir, f))]
print(onlyfiles)

for files in onlyfiles:
   img = image.load_img(test_dir+files,target_size=(28,28))
   x = image.img_to_array(img)
   x = np.expand_dims(x,axis=0)

   images = np.vstack([x])
   # plt.imshow(images)
   classes = model.predict_classes(images,batch_size=3)
   print(classes,files)
   classes = classes[0]


# {'cough': 0, 'healthy': 1}
