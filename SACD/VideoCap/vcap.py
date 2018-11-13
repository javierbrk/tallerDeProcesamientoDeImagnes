import cv2
#from os import walk
#import sys
#import time
import numpy as np

print ("iniciando")
# Camara 1 es la camara web integrada en mi caso
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 1
#iniciar camara
camera = cv2.VideoCapture(0)

# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im

for i in range (fotogramas):
 temp = get_image()
 cv2.imshow("Original", temp)

cv2.waitKey()
