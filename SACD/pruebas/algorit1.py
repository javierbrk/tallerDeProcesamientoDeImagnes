import cv2
import sys
import time
import numpy as np
from matplotlib import pyplot as plt
from os import walk



def _abrir_archivo(images):
    imagen = cv2.imread(images)
    if imagen.any()== None:
       print("No se puede abrir imagen")
       sys.exit(1)
    return imagen

def prueba():

    imagen = _abrir_archivo('images/31.jpg')
    ret,thresh3 = cv2.threshold(imagen,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(imagen,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(imagen,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','TOZERO','TOZERO_INV','TRUNC']
    images = [imagen, thresh4, thresh5, thresh3]

    for i in range(4):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'plasma')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()
    cv2.waitKey(0)

    
