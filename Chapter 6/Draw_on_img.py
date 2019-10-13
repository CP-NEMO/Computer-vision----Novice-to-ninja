import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
# Draw a circle with red color filled inside
cv2.circle(img,(447,63), 63, (0,0,255), -1)
# to draw ellips we need too many arguments 
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[120,31],[172,25],[51,10]], np.int32)
pts = pts.reshape((-1,1,2))
# To Draw polygon
cv2.polylines(img,[pts],True,(0,255,255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
