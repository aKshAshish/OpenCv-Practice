import cv2
import numpy as np

img = cv2.imread('./img/messi.jpg')
rows, cols, channels = img.shape

# Transformation Matrix
pts1 = np.float32([[0,0], [cols, 0], [0, rows], [cols, rows]])
pts2 = np.float32([[rows, 0], [rows, cols], [0, 0], [0, cols]])
M = cv2.getPerspectiveTransform(pts1, pts2)

# Transformation
dst = cv2.warpPerspective(img, M, (rows, cols))
cv2.imshow("Original", img)
cv2.imshow("Transformed", dst)
cv2.waitKey()