import numpy
import cv2

img1 = cv2.imread('black_white_1.png')
img2 = cv2.imread('black_white_2.png')

cv2.imshow('First Image', img1)
cv2.imshow('Second Image', img2)

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
img1_not = cv2.bitwise_not(img1)
img2_not = cv2.bitwise_not(img2)

cv2.imshow('Bitwise AND', bit_and)
cv2.imshow('Bitwise OR', bit_or)
cv2.imshow('Bitwise XOR', bit_xor)
cv2.imshow('Bitwise NOT Image 1', img1_not)
cv2.imshow('Bitwise NOT Image 2', img2_not)

cv2.waitKey(0)
cv2.destroyAllWindows()