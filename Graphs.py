#Initialisation
from os import getcwd, chdir

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés')


import numpy as np
import random
from Graphs import *
from keras.datasets import mnist
from keras import models
from keras import layers
from DataCreationGraph import *
from matplotlib import pyplot as plt


##Fonction reset de l'ia

def reset_ia (model):
    del model
def creer_ia():
    model1 = models.Sequential()
    model1.add(layers.Conv2D(32, (3, 3), activation='relu',
    input_shape=(120, 180, 3)))

    model1.add(layers.MaxPooling2D((2, 2)))
    model1.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model1.add(layers.MaxPooling2D((2, 2)))
    model1.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model1.add(layers.MaxPooling2D((2, 2)))
    model1.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model1.add(layers.MaxPooling2D((2, 2)))
    model1.add(layers.Flatten())
    model1.add(layers.Dense(512, activation='relu'))
    model1.add(layers.Dense(4, activation='softmax'))

    model1.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy'])
    return(model1)


def creer_vecteurs():

    n = len(Vecteurimage)

    Vecteurimageshuffle = np.zeros((n,120,180,3))
    Vecteurimagelabelshuffle = np.zeros((n,4))
    liste= np.array(range(n))
    np.random.shuffle(liste)
    for k in range (n):
        Vecteurimageshuffle[k] = Vecteurimage[liste[k]]
        Vecteurimagelabelshuffle[k] = Vecteurlabelimage[liste[k]]

    k = int(3/4*n)

    Vecteurtrain = np.zeros((k,120,180,3))
    Vecteurlabeltrain = np.zeros((k,4))

    Vecteurtest = np.zeros((n-k,120,180,3))
    Vecteurlabeltest =np.zeros((n-k,4))


    for i in range (k):
        Vecteurtrain[i]= Vecteurimageshuffle[i]
        Vecteurlabeltrain[i]= Vecteurimagelabelshuffle[i]
    for i in range (n-k):
        Vecteurtest[i]= Vecteurimageshuffle[i+k]
        Vecteurlabeltest[i]= Vecteurimagelabelshuffle[i+k]

    return(Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest)



##Traçage de graph



def accuracyepoch (n,model,Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest) :
    Y=[]
    test_loss, test_acc = model.evaluate(Vecteurtest, Vecteurlabeltest)
    Y.append(test_acc)
    for k in range(n) :
        model.fit(Vecteurtrain, Vecteurlabeltrain, epochs=1, batch_size=5)
        test_loss, test_acc = model.evaluate(Vecteurtest, Vecteurlabeltest)
        Y.append(test_acc)
    return(Y)

def accuracyepochm (n,m):
    """ n = nombre d'Epoch, m = nombre de test sur lesquels on fait la moyenne """
    X = range(n+1)
    Ylist = []

    for k in range (m):
        print("\n\n\n\n\n\n")
        print("_____________________________________________")
        print("etape", k+1)
        print("_____________________________________________")
        print("\n\n\n\n\n\n")
        model = creer_ia()
        (Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest) = creer_vecteurs()
        Ylist.append(accuracyepoch(n,model,Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest))
        reset_ia(model)
    Y= []
    for i in range(n+1):
        ym = 0
        for k in range(m):
            ym += Ylist[k][i]
        ym = ym/m
        Y.append(ym)
    plt.plot(X,Y)
    plt.title("Accuracy moyenne en fonction du nombre d'epoch")
    plt.show()
    return(Y)

"""

10h42



"""
##
(Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest) = creer_vecteurs()

plt.imshow(Vecteurtrain[0], interpolation='nearest')
plt.show()

print(Vecteurlabeltrain[0])

plt.imshow(Vecteurtrain[1], interpolation='nearest')
plt.show()

print(Vecteurlabeltrain[1])

plt.imshow(Vecteurtest[0], interpolation='nearest')
plt.show()

print(Vecteurlabeltest[0])
