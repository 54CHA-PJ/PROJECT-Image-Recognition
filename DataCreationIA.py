from os import getcwd, chdir, path, listdir
from PIL import Image as img
import numpy as np
import glob
import random

##Importation des images sur python



chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Chocapic')

Chocapicimage = []

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Chocapicimage.append(im)

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Monster')

Monsterimage = []

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Monsterimage.append(im)


chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\\Nutella')

Nutellaimage = []

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Nutellaimage.append(im)

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Riz')

Rizimage = []

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Rizimage.append(im)



Chocapictestimage = []
Monstertestimage = []
Nutellatestimage = []
Riztestimage = []

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Banque test chocapic')

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Chocapictestimage.append(im)

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Banque test monster')

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Monstertestimage.append(im)

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Banque test nutella')

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Nutellatestimage.append(im)

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Banque test riz')

for filename in glob.glob('*.jpg'):
    im=img.open(filename)

    Riztestimage.append(im)

## Création des vecteur de train

n=len(Chocapicimage)

Chocapictrain = np.zeros((n,120,180,3))
Chocapiclabeltrain = np.zeros((n,4))
for k in range(n):
    Chocapictrain[k]=np.array(Chocapicimage[k])
    Chocapiclabeltrain[k] = np.array([1.,0.,0.,0.])


n=len(Monsterimage)

Monstertrain = np.zeros((n,120,180,3))
Monsterlabeltrain = np.zeros((n,4))
for k in range(n):
    Monstertrain[k]=np.array(Monsterimage[k])
    Monsterlabeltrain[k] = np.array([0.,1.,0.,0.])

n=len(Nutellaimage)

Nutellatrain = np.zeros((n,120,180,3))
Nutellalabeltrain = np.zeros((n,4))
for k in range(n):
    Nutellatrain[k]=np.array(Nutellaimage[k])
    Nutellalabeltrain[k] = np.array([0.,0.,1.,0.])

n=len(Rizimage)

Riztrain = np.zeros((n,120,180,3))
Rizlabeltrain = np.zeros((n,4))
for k in range(n):
  Riztrain[k]=np.array(Rizimage[k])
  Rizlabeltrain[k] = np.array([0.,0.,0.,1.])

 ## Création des vecteur de test

n=len(Chocapictestimage)

Chocapictest = np.zeros((n,120,180,3))
Chocapiclabeltest = np.zeros((n,4))
for k in range(n):
    Chocapictest[k]=np.array(Chocapictestimage[k])
    Chocapiclabeltest[k] = np.array([1.,0.,0.,0.])


n=len(Monstertestimage)

Monstertest = np.zeros((n,120,180,3))
Monsterlabeltest = np.zeros((n,4))
for k in range(n):
    Monstertest[k]=np.array(Monstertestimage[k])
    Monsterlabeltest[k] = np.array([0.,1.,0.,0.])


n=len(Nutellatestimage)

Nutellatest = np.zeros((n,120,180,3))
Nutellalabeltest = np.zeros((n,4))
for k in range(n):
    Nutellatest[k]=np.array(Nutellatestimage[k])
    Nutellalabeltest[k] = np.array([0.,0.,1.,0.])


n=len(Riztestimage)

Riztest = np.zeros((n,120,180,3))
Rizlabeltest = np.zeros((n,4))
for k in range(n):
    Riztest[k]=np.array(Riztestimage[k])
    Rizlabeltest[k] = np.array([0.,0.,0.,1.])



##Creation du vecteur d'image


Vecteurimage = np.concatenate((Chocapictrain,Monstertrain,Nutellatrain,Riztrain))
Vecteurlabelimage = np.concatenate((Chocapiclabeltrain,Monsterlabeltrain,Nutellalabeltrain,Rizlabeltrain))




##Reshape des vecteurs train/test


Vecteurimage = Vecteurimage.astype('float32') / 255



Chocapictest = Chocapictest.astype('float32') / 255


Monstertest = Monstertest.astype('float32') / 255


Nutellatest = Nutellatest.astype('float32') / 255


Riztest = Riztest.astype('float32') / 255



##Permutation des élements des vecteur train pour randomiser le training
n = len(Vecteurimage)

Vecteurimageshuffle = np.zeros((n,120,180,3))
Vecteurimagelabelshuffle = np.zeros((n,4))
liste= np.array(range(n))
np.random.shuffle(liste)
for k in range (n):
    Vecteurimageshuffle[k] = Vecteurimage[liste[k]]
    Vecteurimagelabelshuffle[k] = Vecteurlabelimage[liste[k]]



##Vecteur test/train final :: séparation des données

n = len(Vecteurimage)

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








