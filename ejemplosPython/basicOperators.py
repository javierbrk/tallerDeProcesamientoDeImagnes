import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread("futbol.jpg",3)
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

px = img[100,100]
print ("Rgb (100,100) Pix vector")
print px
# accessing only blue pixel
blue = img[100,100,0] 
print ("Blue Pix")
print blue

# accessing RED value
print img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),250)

# modifying RED value
img.itemset((10,10,1),250)
img.itemset((10,10,0),250)

print img.item(10,10,2)
cv2.namedWindow("altered")
cv2.imshow("altered", img)
k=cv2.waitKey(0)

#number of rows, columns and channels (if image is color)
print img.shape
#number of pixels
print img.size
#Image datatype
print img.dtype
#Image ROI
ball = img[280:340, 330:390]

img[273:333, 100:160] = ball

#Splitting and Merging Image Channels
b,g,r = cv2.split(img)

cv2.namedWindow("RED")
cv2.imshow("RED", r)

cv2.namedWindow("GREEN")
cv2.imshow("GREEN", g)

cv2.namedWindow("BLUE")
cv2.imshow("BLUE", b)

k=cv2.waitKey(0)


img[:,:,2] = 0
img[:,:,1] = 0
cv2.imshow("BLUE", img)
k=cv2.waitKey(0)



