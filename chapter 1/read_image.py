import numpy as np
import cv2

img = cv2.imread('image.jpg',0)#read the image file
cv2.imshow('image',img)#display the image
cv2.waitKey(0)
cv2.destroyAllWindows() #Distroy all the windows when press any key 
