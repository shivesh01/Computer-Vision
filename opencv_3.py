import cv2
import numpy

img =cv2.imread ("photo.png",1)


resized =cv2.resize(img, (300,300))


cv2.imshow("img",resized)
cv2.waitKey(2000)

cv2.destroyAllWindows