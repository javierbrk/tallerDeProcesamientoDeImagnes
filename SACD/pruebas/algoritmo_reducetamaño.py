import cv2 
import sys
from resizeimage import resizeimage
from cv2 import resize
from os import walk
from imutils import contours
import numpy as np
import imutils
import time


def _abrir_archivo(dir):
    imagen = cv2.imread(dir)
    if imagen.any() == None:
        print('No se puede abrir imagen')
        sys.exit(1)
    return imagen


def order_points(pts):
    #Inicializar una lista de coordenadas que pueden ser ordenadas
    #como la primera entrada en la lista al lado izquierdo,
    #la segunda entrada está al lado derecho, la tercera es el
    #botón derecho y la cuarta es el botón izquierdo
    rect = np.zeros((4, 2), dtype = 'float32')

    #El punto del top-izquierdo puede tener una pequeña suma, mientras
    #que el punto del botón derecho puede tener una suma muy larga
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    #ahora, estimar la diferencia entre los puntos, el,
    #punto del top-derecho puede tener la diferencia más pequeña,
    #mientras que el botón izquierdo puede tener la diferencia más larga
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[2] = pts[np.argmax(diff)]

    #Retorna la coordenadas ordenadas
    return rect


def prueba():
    imagen = _abrir_archivo('images/33.jpg')
    imagen2 = cv2.resize(imagen, None, fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('original', imagen)
    cv2.imshow('original', imagen2)
