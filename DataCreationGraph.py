from os import getcwd, chdir, path, listdir
from PIL import Image as img
import numpy as np
import glob
import random
from matplotlib import pyplot as plt
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


##Creation du vecteur d'image


Vecteurimage = np.concatenate((Chocapictrain,Monstertrain,Nutellatrain,Riztrain))
Vecteurlabelimage = np.concatenate((Chocapiclabeltrain,Monsterlabeltrain,Nutellalabeltrain,Rizlabeltrain))

Vecteurimage = Vecteurimage.astype('float32') / 255








