#Initialisation(prend du temps)

import numpy as np
import numpy.random as random
from matplotlib import pyplot as plt
from os import getcwd, chdir
from keras.datasets import mnist
from keras import models
from keras import layers

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés')

from DataCreationIA import *

plt.imshow(Vecteurtrain[0], interpolation='nearest')
plt.show()

print(Vecteurlabeltrain[0])

plt.imshow(Vecteurtrain[1], interpolation='nearest')
plt.show()

print(Vecteurlabeltrain[1])

plt.imshow(Vecteurtest[0], interpolation='nearest')
plt.show()

print(Vecteurlabeltest[0])

##  creation des layers


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
input_shape=(120, 180, 3)))

model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))



model.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])


##  Entrainenment de l'ia

model.fit(Vecteurtrain, Vecteurlabeltrain, epochs=10, batch_size=6)

##Test de l'ia


test_loss, test_acc = model.evaluate(Vecteurtest, Vecteurlabeltest)

print(test_acc)

"""
##

test_loss, test_acc = model.evaluate(Nutellatest, Nutellalabeltest)
print(test_acc)
"""