from os import getcwd, chdir
import cv2
import numpy as np

chdir("C:\\Users\sacha\Desktop\TIPE\capture telephone")
loc = "C:\\Users\sacha\Desktop\DOSSIER TIPE TEST"

def capture(ip= "XXXXXXXXXXXXXXX", directory = loc):

    """
    ex: ip = 192.168.130.122:8080
    __________________etapes:______________________
    1- le programme prend une photo : PhotoAVANT
    2- appuyer sur i
    3- le programme prend une photo : PhotoAPRES
    4- appuyer sur f
    _______________________________________________"""

    url = "http://"+ip+"/video"

    cap = cv2.VideoCapture(url)
    ret,frame = cap.read()
    while(True):
        cv2.imshow('img1',frame)
        if cv2.waitKey(1) & 0xFF == ord('i'):
            cv2.imwrite(directory+'\imageavant.jpg', frame)
            cv2.destroyAllWindows()
            break

    cap.release()

    cap = cv2.VideoCapture(url)
    ret,frame = cap.read()
    while(True):
        cv2.imshow('img1',frame)
        if cv2.waitKey(1) & 0xFF == ord('f'):
            cv2.imwrite(directory+'\imageapres.jpg', frame)
            cv2.destroyAllWindows()
            break

    cap.release()

