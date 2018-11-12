import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread("DSC_0860.JPG",0)
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


