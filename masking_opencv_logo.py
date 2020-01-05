import cv2
import numpy as np

img1 = cv2.imread('./img/roi.jpg')
logo = cv2.imread('./img/opencv_logo.png')
print(img1.shape)
print(logo.shape)

logo = cv2.resize(logo, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

rows, cols, channels = logo.shape
roi = img1[0:rows, 0:cols]

# # # Create mask for region of interest
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_bg = cv2.bitwise_and(logo, logo, mask=mask)

dst = cv2.add(img1_bg, img2_bg)

img1[0:rows, 0:cols] = dst


cv2.imshow("Logo", logo)
cv2.imshow("Mask INV", mask_inv)
cv2.imshow('RoI', roi)
cv2.imshow("Mask", mask)
cv2.imshow('bg1', img1_bg)
cv2.imshow('bg2', img2_bg)
cv2.imshow("dst", dst)
cv2.imshow("Final image", img1)
cv2.waitKey(0)
# cv2.destroyAllWindows()