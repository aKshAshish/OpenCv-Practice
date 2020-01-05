import cv2
import numpy as np

img = cv2.imread("./img/messi.jpg")
rows, cols, channel = img.shape
print(img.shape)
# Transformation Matrix
M = np.float32([[1, 0, 100], [0, 1, 100]])

# Transformation
dst = cv2.warpAffine(img, M, (cols, rows))
print(dst.shape)

cv2.imshow("Original", img)
cv2.imshow("Transformed", dst)
cv2.waitKey(0)