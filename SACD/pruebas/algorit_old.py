import cv2
import sys
from os import walk
import time


def _abrir_archivo(images):
    imagen = cv2.imread(images)
    if imagen == None:
        print('No se puede abrir imagen')
        sys.exit(1)
    return imagen


def prueba():

    imagen = _abrir_archivo('31.jpg')
    cv2.imshow("ventana", imagen)
    cv2.waitKey(0)
    
