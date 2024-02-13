#Initialisation(prend du temps)
from os import getcwd, chdir


chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés')
from DataCreationIA import *
chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés')
from Graphs import *

import numpy as np
import random
from keras.datasets import mnist
from keras import models
from keras import layers
from DataCreationIA import *
from matplotlib import pyplot as plt

import time

## version 2

def accuracynombre ():

    (Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest) = creer_vecteurs()

    n = len(Vecteurlabeltrain)

    k = 10

    L = []

    model = creer_ia()

    while k < n:

        print("\n\n\n\n\n\n\n")
        print(k)
        print("\n\n\n\n\n\n\n")

        vtrain = Vecteurtrain[k-5:k]
        vlabeltrain = Vecteurlabeltrain[k-5:k]
        model.fit(vtrain, vlabeltrain, epochs=3, batch_size=2)

        test_loss, test_acc = model.evaluate(Vecteurtest, Vecteurlabeltest)

        print(test_acc)

        L.append(test_acc)

        k = k + 5

    reset_ia(model)

    return(L)



def test_accuracynombre(n):

    t1 = time.localtime()
    print("heure de debut:", t1[3],"heures, ", t1[4], "minutes", t1[5], "secondes")

    Ylist = []

    for k in range(n):
        print("\n\n\n\n\n\n\n")
        print("IA n°", k)
        print("\n\n\n\n\n\n\n")
        L = accuracynombre()
        Ylist.append(L)

    Y=[]

    for i in range(len(Ylist[0])):
        ym = 0
        for k in range(n):
            ym += Ylist[k][i]
        ym = ym/n
        Y.append(ym)

    X = [5+ k*5 for k in range(len(L))]

    t2 = time.localtime()

    print("debut:", t1[3],"heures, ", t1[4], "minutes", t1[5], "secondes")
    print("fin:", t2[3],"heures, ", t2[4], "minutes", t2[5], "secondes")

    s=str(n)
    text = "Accuracy en fonction du nombre d'images\n Moyenne faite sur n test: n= "+s
    plt.plot(X,Y)
    plt.title(text)
    plt.show()


"""
pour 30 images avec deltak = 5, batch = 2, epoch = 3:

prend 15 min
"""





## ancienne version
"""
n = len(Vecteurlabeltrain)

(Vecteurtrain,Vecteurlabeltrain,Vecteurtest,Vecteurlabeltest) = creer_vecteurs()

k = 10

L = []
while k < n:

    print("\n\n\n\n\n\n\n")
    print(k)
    print("\n\n\n\n\n\n\n")

    model = creer_ia()

    vtrain = Vecteurtrain[:k]
    vlabeltrain = Vecteurlabeltrain[:k]
    model.fit(vtrain, vlabeltrain, epochs=5, batch_size=2)

    test_loss, test_acc = model.evaluate(Vecteurtest, Vecteurlabeltest)

    print(test_acc)

    L.append(test_acc)

    reset_ia(model)

    k = k + 10
"""


