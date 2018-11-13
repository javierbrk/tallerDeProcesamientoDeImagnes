import cv2
import sys
import time
from os import walk



def _abrir_archivo(images):
    imagen = cv2.imread(images)
    #if imagen == None:
    if imagen.any()== None:
        print("No se puede abrir imagen")
        sys.exit(1)
    return imagen

def prueba():

    imagen = _abrir_archivo('images/2.jpg')
    ret,imagen2 = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)
    cv2.imshow("ventana2", imagen2)
    #cv2.imshow("ventana", imagen)
    cv2.waitKey(0)
