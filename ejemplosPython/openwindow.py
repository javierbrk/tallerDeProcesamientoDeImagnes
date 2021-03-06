import numpy as np
import cv2

def abrirVentana():
	img = cargarImagen()
	# Load an color image in grayscale
	cv2.startWindowThread()
	cv2.namedWindow("preview")
	cv2.imshow("preview", img)
	k=cv2.waitKey(0)
	print(k)
	if k == 27:         # wait for ESC key to exit
		cv2.destroyAllWindows()
	elif k == 115: # wait for 's' key to save and exit
		cv2.destroyAllWindows()
		print(k)
		cv2.imwrite("DSC_0860_gis.png",img)


def cargarImagen():
	"""Funcion que carga la imagen de mesi."""
	return cv2.imread("./futbol.jpg",3)
