import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('D:\\Project\\dataset\\dataset\\train\\Apple___Apple_scab\\08c42d78-aa7b-4106-b0c1-b260f898dcba___FREC_Scab 3151.JPG',0)

cv2.imshow('Output Gray Scale Image', img)
cv2.imshow('Output Gray Scale Image', img)

img = cv2.GaussianBlur(img,(3,3),0)

cv2.waitKey(0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.destroyAllWindows()

