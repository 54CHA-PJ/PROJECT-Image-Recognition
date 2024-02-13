from os import chdir

chdir('C:\\Users\sacha\Desktop\TIPE\programmes utilisés')

from convertpng import *

## comparateur d'image, version finale

def difference(img1, img2, N=5, eps = 30 ,b = 0):
    """
    (array image AVANT en N/B 255, array image APRES en N/B 255, N = facteur de réduction, eps = valeur seuil de différence entre deux pixels (entre 0 et 255), b = largeur de la bordure)
    -> matrice numpy (difference entre les deux images)
    """

    """N, eps, b sont des valeurs à prérégler en fonction de l'environnement du garde manger, plus précisément:

    N = nombre de fois qu'on divise la taille des images par 2 AVANT de les comparer (ce qui permet de eviter les problemes de décalage entre les deux images)

    (hauteur,largeur) -> (int(hauteur*2^-N), int(largeur*2^-N))

    eps = valeur seuil de pixel à partir laquelle on admet qu'il y a une différence entre les deux pixels des deux images

    b = nombre de pixels a ajouter autour des coordonnées initiales pour éviter une coupure 'trop brute'
    """

    p1 = np.array(img1)
    p2 = np.array(img2)

    if p1.shape != p2.shape:
        print("les deux images ne sont pas de la même taille")

    print("0/2")
    p1g = grayscale(p1)
    print("1/2")
    p2g = grayscale(p2)
    print("2/2")

    p1r = reductionx(p1g, N)

    p2r = reductionx(p2g, N)

    n = len(p1r)
    m = len(p1r[0])





    a = [[0 for j in range(m)] for k in range(n)]

    for k in range(n):
        for j in range(m):
            if abs(p1r[k][j] - p2r[k][j]) > eps:
                a[k][j] = p1r[k][j]

    ((xmin,ymin),(xmax,ymax))=recupererxbord(p1g, a, N, b)

    plt.title("différence (grossièrement):")
    plt.imshow(a,cmap=plt.cm.binary)
    plt.show()

    return np.array(p1)[ymin:ymax, xmin:xmax]




def difference2(img1, img2, N=5, eps = 30 ,b = 0):
    """même chose que la fonction difference mais n'affiche rien"""
    p1 = np.array(img1)
    p2 = np.array(img2)
    if p1.shape != p2.shape:
        print("les deux images ne sont pas de la même taille")
    p1g = grayscale(p1)
    p2g = grayscale(p2)
    p1r = reductionx(p1g, N)
    p2r = reductionx(p2g, N)
    n = len(p1r)
    m = len(p1r[0])
    a = [[0 for j in range(m)] for k in range(n)]
    for k in range(n):
        for j in range(m):
            if abs(p1r[k][j] - p2r[k][j]) > eps:
                a[k][j] = p1r[k][j]
    ((xmin,ymin),(xmax,ymax))=recupererxbord(p1g, a, N, b)
    return np.array(p1)[ymin:ymax, xmin:xmax]






# fontions 'récuperer' et 'recupererxbord'
# explicitées à la page suivante:







## récupération des coordonnées initiales et ajout du bord

def recupererxbord(img,mr,N,b):
    """img = matrice d'image initiale, mr = matrice reduite, N = coefficient de reduction, b = largeur du bord dans la matrice d'origine
    -> donne les coordonnes de recoupage dans la matrice INITIALE (avant d'etre reduite)
    -> ajout de la bordure d'image
    """
    (xmin,ymin),(xmax,ymax) = recuperer(mr)

    f = 2**N
    ((x1,y1),(x2,y2)) = recuperer(mr)
    ((xmin,ymin),(xmax,ymax)) = ((f*x1,f*y1),(f*x2,f*y2))

    if xmin <b:
        xmin = 0
    else:
        xmin = xmin-b
    if ymin <b:
        ymin = 0
    else:
        ymin = ymin-b
    if xmax+b >= len(img[0]):
        xmax = len(img[0])-1
    else:
        xmax = xmax+b
    if ymax+b >= len(img):
        ymax = len(img)-1
    else:
        ymax = ymax+b

    c1 = (int(xmin),int(ymin))
    c2 = (int(xmax),int(ymax))

    #print(c1,c2)
    return(c1,c2)


def recuperer(m):
    #'retire les zeros' de la matrice d'empreinte et
    #renvoie les coordonnees de l'objet dans l'image réduite

    ymin, xmin = float("inf"),float("inf")
    ymax, xmax = -float("inf"),-float("inf")

    for k in range(len(m)):
        for j in range(len(m[0])):
            if m[k][j] != 0:
                xmin = min(xmin, j)
                xmax = max(xmax,j)
                ymin = min(ymin, k)
                ymax = max(ymax,k)
    return((xmin,ymin),(xmax,ymax))