#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Cargando / importando las librerías
import cv2
import sys
import time
import numpy as np
import imutils
from os import walk
from imutils import contours
#import threading



#Definiendo la funcion que nos permite abrir la imagen capturada
def _abrir_archivo(dir):
    imagen = cv2.imread(dir)
    if imagen.any() == None:
        print("No se puede abrir imagen")
        sys.exit(1)
    return imagen

#Denifiniendo las coordenadas de la lista de entradas
def order_points(pts):
	# inicializa las coordenadas que se puede listar ordenandola como
	# la primera entrada de en el listado sera el top-left,
	# la segunda entrada es el top-right, la tercera es el bottom-right
	# y la cuarta es el bottom-left

	rect = np.zeros((4, 2), dtype = "float32")

	# En el punto para el top-left point es posible que se deba realizar una
    #pequeña suma, mientras que el punto del bottom-right puede tener una
    #suma larga
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# Ahora, digitalizamos la diferencia de los puntos, el punto top-right
	# puede tener una ligera diferencia,mientras que la diferencia en el punto
	# bottom-left puede ser mayor
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	# return the ordered coordinates
	return rect

def four_point_transform(image, pts):
	# obtain a consistent order of the points and unpack them
	# individually
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return warped

# Definiendo la función para el 7 segmento:
def prueba(imagen):
    DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9 }

    a = False
    #imagen = _abrir_archivo()
    height, width, channels = imagen.shape
    print("valores originales A H C: ")
    print(height, width, channels)
    fc = 1
    if width > 1000 :
        fc =.1
    elif width > 500 :
        fc =.5
    imagen2 = imutils.resize(imagen, height=500)
    #imagen2 = cv2.resize(imagen,None,fx=fc, fy=fc, interpolation = cv2.INTER_CUBIC)

    gray = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)

    height, width, channels = imagen2.shape
    print("valores de alto, ancho, canales: ")
    print(height, width, channels)



    # Encuentra los contornos y los ennumera
    # en orden decendiente de tamaño
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    displayCnt = None

    # para cada contorno en el la lista de contornos
    for c in cnts:
        # verifica
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        print("contornos de corte:")
        print(approx)
        # si cuatro lados lo desplegara
        if len(approx) == 4:
            print("<------Existe una funcional 4 lados")
            displayCnt = approx
            break

    #marcas de corte
    warped = four_point_transform(gray, displayCnt.reshape(4, 2))
    output = four_point_transform(imagen2, displayCnt.reshape(4, 2))


    height, width, channels = output.shape
    print("valores recortado de alto, ancho, canales: ")
    print(height, width, channels)
    if height < 50:
        output = imutils.resize(output, height=75)
        warped  = imutils.resize(warped, height=75)

    if height > 80:
        output = imutils.resize(output, height=75)
        warped  = imutils.resize(warped, height=75)
    #ajuste de brillo
    alpha = float(2.5)
    #cv2.equalizeHist(
    adjust =cv2.multiply(warped, np.array([alpha]))

    thresh2 = cv2.threshold(adjust, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    thresh3 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
    #/////////

    thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)


    #///////////////////aproxima2
    estirado = cv2.inRange(adjust, 10, 140)


    cnts = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
    print("encuentra contornos: ")
    print(len(cnts))
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    print("encuentra contornos imutils.is_cv2: ")
    print(len(cnts))
    digitCnts = []

    # loop over the digit area candidates
    try:
        for c in cnts:
            # compute the bounding box of the contour
            (x, y, w, h) = cv2.boundingRect(c)
            if w >=15 and (h>=30 and h<=40):
                digitCnts.append(c)
        digitCnts = contours.sort_contours(digitCnts,method="left-to-right")[0]
        digits = []

        for c in digitCnts:

            (x, y, w, h) = cv2.boundingRect(c)
            roi = thresh[y:y + h, x:x + w]

            # compute the width and height of each of the 7 segments
            # we are going to examine
            (roiH, roiW) = roi.shape
            (dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
            dHC = int(roiH * 0.05)

            # define the set of 7 segments
            segments = [
                ((0, 0), (w, dH)),	# top
                ((0, 0), (dW, h // 2)),	# top-left
                ((w - dW, 0), (w, h // 2)),	# top-right
                ((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
                ((0, h // 2), (dW, h)),	# bottom-left
                ((w - dW, h // 2), (w, h)),	# bottom-right
                ((0, h - dH), (w, h))	# bottom
            ]
            on = [0] * len(segments)

            # loop over the segments
            for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
                # extract the segment ROI, count the total number of
                # thresholded pixels in the segment, and then compute
                # the area of the segment
                segROI = roi[yA:yB, xA:xB]
                total = cv2.countNonZero(segROI)
                area = (xB - xA) * (yB - yA)

                # if the total number of non-zero pixels is greater than
                # 50% of the area, mark the segment as "on"
                if area == 0:
                    area =0.001

                if total / float(area) > 0.5:
                    on[i]= 1

            # lookup the digit and draw it on the image
            digit = DIGITS_LOOKUP[tuple(on)]
            digits.append(digit)
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(output, str(digit), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

        # display the digits

        print(u"{}{}.{} \x57 \x50 \x77".format(*digits))

        print("respuesta: ")
        print(len(digitCnts))
        print(len(digitCnts[0]))

    except Exception as e:
        print(e)

    cv2.imshow("original", imagen2)
    cv2.imshow("recortado", output)
    cv2.imshow("ajustado", adjust)
    cv2.imshow("estirado", estirado)
    cv2.imshow("ventana4", thresh3)
    cv2.imshow("ventana2", thresh)
    cv2.imshow("ventana3", thresh2)

    cv2.waitKey(0)
