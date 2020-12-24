import cv2
import numpy

img =cv2.imread ("photo.png",1)


resized =cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))


cv2.imshow("img",resized)
cv2.waitKey(2000)

cv2.destroyAllWindows