from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

## fonctions pour convertir une matrice couleur en monochrome

def moyenne3(t):
    """ t = tableau de taille 3 (plus optimal) + inversion des valeurs des pixels """
    return (255 - ( int(t[0]) + int(t[1]) + int(t[2]) )//3)

def moyenne(t):
    """moyenne des valeurs de t, un tableau de taille quelconque """
    s = 0
    n = len(t)
    for k in range(n):
        s += t[k]
    return (s//n)

def grayscale(ar):
    n = len(ar)
    m = len(ar[0])

    u = [[0 for k in range(m)] for k in range(n)]

    for i in range(n):
        if i%((n*5)//100) == 0:
            print("traitement", int(100* i/n), "%")
            #pour suivre l'avancement du traitement (qui prend parfois 2 minutes)
        t = ar[i]
        for k in range(m):
            l = list(t[k])
            u[i][k] = moyenne3(l)
    return(np.array(u))


##  completer une matrice numpy de dimension (hi,li) en une matrice de dimension (hi,lf)


def complete_largeur(mat,lf):
    """ np.array de dimension (hi,li), (hauteur,largeur) de sortie tq
        largeur de sortie (lf) >= largeur d'entrée (li)"""
    s = mat.shape

    if len(s) == 2:
        #matrice monochromatique
        (hi,li) =  s
        res = np.zeros((hi,lf), int)
        dist = (lf-li)//2
        #on va mettre l'image initiale (image brute) au milieu de l'image finale (image élargie des deux côtés)
        for k in range(hi):
            for j in range(lf):
                if j < dist:
                    res[k][j] = mat[k][0]
                elif j >= dist+li-1:
                    res[k][j] = mat[k][li-1]
                else:
                    res[k][j] = mat[k][j-dist]
        return res

    elif len(s) == 3:
        #matrice couleur
        (hi,li,a) =  s
        #on va mettre l'image initiale (image brute) au milieu de l'image finale (image élargie des deux côtés)
        res = np.array([[np.zeros(3, int) for k in range(lf)]for j in range(hi)])
        dist = (lf-li)//2

        for k in range(hi):
            for j in range(lf):
                if j < dist:
                    res[k][j] = mat[k][0]
                elif j >= dist+li-1:
                    res[k][j] = mat[k][li-1]
                else:
                    res[k][j] = mat[k][j-dist]
        return res

## réduction des matrices (paramètre N)

def reduction(mat):
    n = len(mat)//2
    m = len(mat[0])//2

    t = [[0 for j in range(m)] for k in range(n)]

    for k in range(n):
        for j in range(m):
            c = (mat[2*k][2*j], mat[2*k][2*j+1], mat[2*k+1][2*j], mat[2*k+1][2*j+1])
            t[k][j] = moyenne(c)
    return(t)

def reductionx(mat, N):
    temp = mat
    #on reduit N fois la matrice (en divisant sa taille par 2 à chaque itération)
    for k in range(N):
        temp = reduction(temp)
    return(temp)




## fonctions finalement pas utilisées


def cambouis(mat, dim):
    """découpe la matrice (m,n) pour en extraire une de taille < (dim*dim)"""
    a = np.array([[mat[0][0] for j in range(dim)] for k in range(dim)] )
    n = min(len(mat), dim)
    p = min(len(mat[0]), dim)

    for i in range(n):
        for j in range(p):
            a[i][j] = mat[i][j]

    return(a)

def filtrenoir(mat):
    #filtre passe bas pour une matrice monochromatique
    f = mat.copy()
    for k in range(len(mat)):
        for j in range(len(mat[0])):
            if f[k][j] < 120:
                f[k][j] = 0
    return(f)

def reductionmax(mat, dim):
    """reduit la matrice jusqu'a ce que sa taille soit < à (dimxdim)"""
    m = min(len(mat),len(mat[0]))
    #print(m)
    a = suppuiss2(m, dim)
    #print(a)
    if a == -1:
        print("la matrice est deja plus petite que dim*dim")
    if a == 0:
        return(mat)
    else:
        return(reductionx(mat, a+1))

def suppuiss2(m, dim):
    #on cherche l'entier k le plus grand qui laisse m//(2**k) superieur a dim, m entier
    k=-1
    while m//(2**k) >= dim:
        k +=1
    return(k-1)