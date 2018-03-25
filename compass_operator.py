import cv2
import numpy as np

img = cv2.imread('Lenna.png',0)
img = np.float32(img)

final_filtered = img.copy()

h = np.array(([1,1,0],[1,0,-1],[0,-1,-1]), dtype="float32")
filteredImg1 = cv2.filter2D(img,-1,h) 
filteredImg1 = abs(filteredImg1)
filteredImg1 = filteredImg1 / np.amax(filteredImg1[:])

h = np.array(([1,1,1],[0,0,0],[-1,-1,-1]), dtype="float32")
filteredImg2 = cv2.filter2D(img,-1,h) 
filteredImg2 = abs(filteredImg2)
filteredImg2 = filteredImg2 / np.amax(filteredImg2[:])

h = np.array(([0,1,1],[-1,0,1],[-1,-1,0]), dtype="float32")
filteredImg3 = cv2.filter2D(img,-1,h) 
filteredImg3 = abs(filteredImg3)
filteredImg3 = filteredImg3 / np.amax(filteredImg3[:])

h = np.array(([1,0,-1],[1,0,-1],[1,0,-1]), dtype="float32")
filteredImg4 = cv2.filter2D(img,-1,h) 
filteredImg4 = abs(filteredImg4)
filteredImg4 = filteredImg4 / np.amax(filteredImg4[:])

h = np.array(([-1,0,1],[-1,0,1],[-1,0,1]), dtype="float32")
filteredImg5 = cv2.filter2D(img,-1,h) 
filteredImg5 = abs(filteredImg5)
filteredImg5 = filteredImg5 / np.amax(filteredImg5[:])

h = np.array(([0,-1,-1],[1,0,-1],[1,1,0]), dtype="float32")
filteredImg6 = cv2.filter2D(img,-1,h) 
filteredImg6 = abs(filteredImg6)
filteredImg6 = filteredImg6 / np.amax(filteredImg6[:])

h = np.array(([-1,-1,-1],[0,0,0],[1,1,1]), dtype="float32")
filteredImg7 = cv2.filter2D(img,-1,h) 
filteredImg7 = abs(filteredImg7)
filteredImg7 = filteredImg7 / np.amax(filteredImg7[:])

h = np.array(([-1,-1,0],[-1,0,1],[0,1,1]), dtype="float32")
filteredImg8 = cv2.filter2D(img,-1,h) 
filteredImg8 = abs(filteredImg8)
filteredImg8 = filteredImg8 / np.amax(filteredImg8[:])

cv2.imshow("Filtered Image 1", filteredImg1)
cv2.imshow("Filtered Image 2", filteredImg2)
cv2.imshow("Filtered Image 3", filteredImg3)
cv2.imshow("Filtered Image 4", filteredImg4)
cv2.imshow("Filtered Image 5", filteredImg5)
cv2.imshow("Filtered Image 6", filteredImg6)
cv2.imshow("Filtered Image 7", filteredImg7)
cv2.imshow("Filtered Image 8", filteredImg8)

h = np.array(([1,1,0],[1,0,-1],[0,-1,-1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([1,1,1],[0,0,0],[-1,-1,-1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([0,1,1],[-1,0,1],[-1,-1,0]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([1,0,-1],[1,0,-1],[1,0,-1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([-1,0,1],[-1,0,1],[-1,0,1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([0,-1,-1],[1,0,-1],[1,1,0]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([-1,-1,-1],[0,0,0],[1,1,1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

h = np.array(([-1,-1,0],[-1,0,1],[0,1,1]), dtype="float32")
final_filtered = cv2.filter2D(final_filtered,-1,h) 
final_filtered = abs(final_filtered)
final_filtered = final_filtered / np.amax(final_filtered[:])

edgeSum1 = cv2.add(np.power(filteredImg1,2), np.power(filteredImg2,2), np.power(filteredImg3,2))
edgeSum2 = cv2.add(np.power(filteredImg6,2), np.power(filteredImg7,2), np.power(filteredImg8,2)) 
edgeSum = cv2.add(edgeSum2,edgeSum1)
ret,thresh = cv2.threshold(edgeSum,0.05,1,cv2.THRESH_BINARY)

cv2.imshow("Final filtered:", final_filtered)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()