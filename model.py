#!/usr/bin/env python
# coding: utf-8
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('data/train',target_size=(64, 64),batch_size=5,color_mode='grayscale',class_mode='categorical')
test_set = test_datagen.flow_from_directory('data/test',target_size=(64,64), color_mode='grayscale',class_mode='categorical') 
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
classifier = Sequential()
classifier.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=6, activation='softmax')) # softmax for more than 2
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 
x=1
history=classifier.fit_generator(training_set,steps_per_epoch=600,epochs=x,validation_data=test_set,validation_steps=30)
acc=history.history['val_accuracy'][0]
acc=(int(round(acc,2) * 100))                                       
file=open("acc.txt","w")
pp=str(acc)
file.write(pp)
file.close()
