from os import chdir, getcwd
from PIL import Image
from matplotlib import pyplot as plt
import glob


def resizedir(dir,largeur,hauteur = 0, marque = ''):
    """dir = lien de l'image, largeur a introduire, hauteur facultative (sinon proportionnelle), marque = eventuel indice qui sera mis à la fin du nom du fichier pour mieux le repérer"""

    img = Image.open(dir)

    if hauteur == 0:
        w = (largeur/float(img.size[0]))
        # w = rapport largeur finale/largeur initiale
        hauteur = int((float(img.size[1])*float(w)))

    img = img.resize((largeur,hauteur), Image.ANTIALIAS)
    img.save(dir + marque +'_reshaped.jpg')
    #je rajoute le terme 'reshaped' dans le nom pour identifier les images qui sont au bon format



def resizejpg(img,largeur,hauteur, marque = ''):
    """ img = image qu'on veur adimensionner,
    -> la fonction fait exactement la meme chose que 'resizedir' et sauvegarde l'image dans la localisation ou l'on se situe (dernier chdir("_"))"""

    if hauteur == 0:
        w = (largeur/float(img.size[0]))
        # w = rapport largeur finale/largeur initiale
        hauteur = int((float(img.size[1])*float(w)))

    img = img.resize((largeur,hauteur), Image.ANTIALIAS)
    img.save(marque+'_reshapejpg.jpg')



def vertical_resizejpg(img, hauteur):
    """ ne modifie pas l'element, elle le renvoie"""*

    h = (hauteur/float(img.size[1]))
    # h = rapport hauteur finale/hauteur initiale
    largeur = int((float(img.size[0])*float(h)))

    img = img.resize((largeur,hauteur), Image.ANTIALIAS)
    #faire gaffe
    return(img)



## traitements réalisés sur un groupe d'images (dans un dossier)


def folder_resize(dir, hauteur, largeur, tag = ''):
    """
    exemple dir = 'C:\\Users\sacha\Desktop\DOSSIER TIPE TEST\convertir', tag = 'test'
    """
    chdir(dir)
    for filename in glob.glob('*.jpg'):
        test = Image.open(filename)
        mat = np.array(vertical_resizejpg(test, hauteur))
        fin = complete_largeur(mat, largeur)
        img = Image.fromarray(fin.astype('uint8'), 'RGB')
        img.save(tag+filename+'reshaped.jpg')

















































## a essayer pour vérifier que le code marche


"""


#resize('monster_can_test.jpg', 480)

#resize2('monster_can_test.jpg', 480, 320)

#img = Image.open(lien)
#resize2jpg(img,480,320, marque = '')

#dir = 'C:\\Users\sacha\Desktop\TIPE\programmes utilisés\Monster_can_before'
#bundle_resize(dir, 480, 320)


dir = "C:/Users/sacha/Desktop/TIPE/programmes utilisés/test.jpg"
test = Image.open(dir)

#resize en choisissant la largeur
resizedir(dir,480,0)
x = Image.open("C:/Users/sacha/Desktop/TIPE/programmes utilisés/test.jpg_reshaped.jpg")

plt.title("application du programme resize_jpg sur cette image:")
plt.imshow(x)
plt.show()

##
#resize en choisissant la hauteur et la largeur (déforme l'objet)
resizedir(dir, 480, 320)
z = Image.open("C:/Users/sacha/Desktop/TIPE/programmes utilisés/test.jpg_reshaped.jpg")

#resize en choisissant la hauteur
y = vertical_resizejpg(test, 320)

print(test.size)
print(x.size)
print(y.size)
print(z.size)

f, ax = plt.subplots(1,2)

ax[0].imshow(test, cmap=plt.cm.binary)
ax[0].title.set_text('original'+' ' + str(test.size[0]) + 'x' + str(test.size[1]))
ax[1].imshow(z, cmap=plt.cm.binary)
ax[1].title.set_text('resize dans le format cherché' +' ' + str(z.size[0]) + 'x' + str(z.size[1]))

plt.show()


f, ax = plt.subplots(1,3)

ax[0].imshow(test, cmap=plt.cm.binary)
ax[0].title.set_text('original'+' ' + str(test.size[0]) + 'x' + str(test.size[1]))
ax[1].imshow(y, cmap=plt.cm.binary)
ax[1].title.set_text('vertical resize'+' ' + str(y.size[0]) + 'x' + str(y.size[1]))
ax[2].imshow(x, cmap=plt.cm.binary)
ax[2].title.set_text('horizontal resize'+' ' + str(x.size[0]) + 'x' + str(x.size[1]))

plt.show()

"""
