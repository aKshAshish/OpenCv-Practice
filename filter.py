import cv2
import numpy as np

img = cv2.imread("./img/messi.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Define filter
f = np.float32([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Filter
dst = cv2.filter2D(img_gray, -1, f)
dst_gauss = cv2.GaussianBlur(img, (3,3), 0)
dst_average = cv2.blur(img, (3,3))

cv2.imshow("Original", img)
cv2.imshow("Transformed", dst)
cv2.imshow("Gauss", dst_gauss),
cv2.imshow("Avg", dst_average)
cv2.waitKey(0)