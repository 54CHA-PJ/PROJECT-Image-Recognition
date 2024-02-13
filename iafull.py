#           attention, lancer petit a petit chaque partie
#          ->  il est recommandé d'ouvrir avec pyzo

import numpy as np

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from keras import models
from keras import layers


from tensorflow.keras.utils import to_categorical

images_officiel = test_images.copy()
#test.images sera modifié (a cause de astype) donc on fait une copie des matrices des chiffres au besoin

np.set_printoptions(linewidth=999999999)
#meilleur affichage

##  creation des layers


network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])

##  affichage avant astype
print("\n","\n")
print("\n","\n")
print("image avant 'astype':")
print("\n","\n")

print(train_images[0])
print("\n","\n")
train_images = train_images.reshape((60000, 28 * 28))

##  affichage apres astype
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
print("\n","\n")
print("\n","\n")
print("image apres 'astype':")
print("\n","\n")
print(train_images[0])
print("\n","\n")

##  REDUCTION DE LA MATRICE D'ENTRAINEMENT

#train_images, train_labels = train_images[0:10000], train_labels[0:10000]

##  entrainement de l'ia

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)

##  FONCTION POUR TEST L'IA SUR UNE MATRICE EN PARTICULIER

def iatest(matrice, label):
    """ (matrice numpy, array numpy sous la forme 00000010000"""
    test = np.array([matrice])
    test_l = np.array([label])
    test.shape
    test_l.shape
    r1, r2 = network.evaluate(test, test_l)
    return(r2)

def iafail(matrice,label):
    """ teste tous les label jusqua ce que ça marche"""
    n = len(label)
    a = np.zeros((n, n), float)
    np.fill_diagonal(a, 1.0)
    k = -1
    while k<n:
        k +=1
        t = iatest(matrice, a[k])
        if int(t) == 1:
            break
    if k == -1 :print("erreur")
    print("\n\nJe devais reconnaitre le label:" , label)
    print("J'ai reconnu le label:         " , a[k])


def evalue(m):
    """m = matrice AVANT astype"""
    a = np.array([m])
    a = a.reshape((len(a), 28 * 28))
    a = a.astype('float32') / 255
    return(network.predict(a))

def prediction(m):
    res = evalue(m)[0]
    indice = 0
    p = 0
    for k in range(len(res)):
        if res[k] > p:
            indice = k
            p = res[k]
    return(indice, p)




