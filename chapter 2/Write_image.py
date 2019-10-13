import cv2

img=cv2.imread('image.jpg',120)
cv2.imwrite('image2.png',img)# this function will save the read image into the format we have read it.
