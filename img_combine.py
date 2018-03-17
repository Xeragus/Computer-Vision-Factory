import numpy
import cv2

logo = cv2.imread('arsenal.png')
auba = cv2.imread('auba.jpg')

rows,cols,channels = logo.shape
roi = auba[0:rows, 0:cols]

logo_grey = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_grey, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
auba_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
logo_fg = cv2.bitwise_and(logo, logo, mask = mask)

dst = cv2.add(auba_bg, logo_fg)
auba[0:rows, 0:cols] = dst


cv2.imshow('mask-inv', auba)

cv2.waitKey(0)
cv2.destroyAllWindows()