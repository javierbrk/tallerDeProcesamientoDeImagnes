import numpy as np
import cv2
import os

from openwindow import cargarImagen

def test_cargarImagen ():
    cwd = os.getcwd()
    print (cwd)
    img = cargarImagen()
    assert not(img is None)
