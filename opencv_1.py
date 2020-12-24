import cv2
import numpy

img =cv2.imread ("photo.png",1)


cv2.imshow("img",img)
cv2.waitKey(2000)

cv2.destroyAllWindows