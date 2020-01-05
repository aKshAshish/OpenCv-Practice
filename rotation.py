import cv2
import numpy as np

img = cv2.imread('./img/messi.jpg')
rows, cols, channels = img.shape

# Transformation Matrix
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

# Transformation
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Transformed", dst)
cv2.waitKey(0)