#Color Filter, COlor Space
#Hue : 0  - 180, Saturation : 0 - 255, Value : 0 - 255
import cv2

img = cv2.imread('D:\\Project\\dataset\\dataset\\train\\Apple___Apple_scab\\08c42d78-aa7b-4106-b0c1-b260f898dcba___FREC_Scab 3151.JPG')

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV CONVERTED IMAGE", img_HSV)

cv2.imshow("Hue Channel", img_HSV[:,:,0])

cv2.imshow("Saturation Channel", img_HSV[:,:,1])

cv2.imshow("Value Channel", img_HSV[:,:,2])

cv2.waitKey(0)

cv2.destroyAllWindows()

