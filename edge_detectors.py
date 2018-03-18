import numpy
import cv2

img = cv2.imread('panda.jpg', cv2.IMREAD_GRAYSCALE)
blured_img = cv2.GaussianBlur(img, (5, 5), 0)
sobelx = cv2.Sobel(blured_img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(blured_img, cv2.CV_64F, 0, 1)
laplacian = cv2.Laplacian(blured_img, cv2.CV_64F, ksize=3)
laplacian2 = cv2.Laplacian(blured_img, cv2.CV_64F, ksize=1)
canny = cv2.Canny(img, 100, 150)	
canny2 = cv2.Canny(img, 100, 200)
canny3 = cv2.Canny(img, 150, 200)
cv2.imshow("Image", img)
#cv2.imshow("Sobel X", sobelx)
#cv2.imshow('Sobel Y', sobely)
#cv2.imshow("Laplacian", laplacian)
#cv2.imshow("Laplacian2", laplacian2)
cv2.imshow("Canny", canny)
cv2.imshow("Canny2", canny2)
cv2.imshow("Canny3", canny3)

cv2.waitKey(0)
cv2.destroyAllWindows()