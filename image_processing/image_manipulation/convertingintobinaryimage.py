import cv2

img = cv2.imread('D:\\Project\\dataset\\dataset\\train\\Apple___Apple_scab\\08c42d78-aa7b-4106-b0c1-b260f898dcba___FREC_Scab 3151.JPG',0)

cv2.imshow('Output Gray Scale Image', img)

cv2.waitKey(0)

ret , bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw)

cv2.waitKey(0)

cv2.destroyAllWindows()

