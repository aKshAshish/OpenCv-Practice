import cv2
import numpy as np

img1 = cv2.imread('./img/beach.jpg')
img2 = cv2.imread('./img/forest.jpg')
print(img1.shape)
print(img2.shape)

img3 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Blended Image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()