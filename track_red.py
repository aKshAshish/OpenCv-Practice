# Tracking red color object using mask
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR 2 HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of color
    lower_red = np.array([0, 150, 150])
    upper_red = np.array([20, 255, 255])
    # Mask
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise and with mask
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Video", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Object", res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
