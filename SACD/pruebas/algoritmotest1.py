import cv2
import sys
import time
import numpy as np
from matplotlib import pyplot as plt
from os import walk



def _abrir_archivo(images):
    imagen = cv2.imread(images)
    #if imagen == None:
    if imagen.any()== None:
        print("No se puede abrir imagen")
        sys.exit(1)
    return imagen

def prueba():

    imagen = _abrir_archivo('images/11.jpg')
    #ret,imagen2 = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)
    #ret,imagen2 = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY_INV)
    ret,imagen2 = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY_INV)
    #ret,thresh3 = cv2.threshold(imagen,127,255,cv2.THRESH_TRUNC)
    #ret,thresh4 = cv2.threshold(imagen,127,255,cv2.THRESH_TOZERO)
    #ret,thresh5 = cv2.threshold(imagen,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','TRUNC','BINARY_INV']
    images = [imagen, imagen2, thresh2]

    for i in range(2):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
    #cv2.imshow("ventana2", imagen2)
    #cv2.imshow("ventana", imagen)
    cv2.waitKey(0)

    
