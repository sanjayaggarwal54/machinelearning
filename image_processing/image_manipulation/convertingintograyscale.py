img = cv2.imread('D:\\Project\\dataset\\dataset\\train\\Apple___Apple_scab\\08c42d78-aa7b-4106-b0c1-b260f898dcba___FREC_Scab 3151.JPG')

cv2.imshow('Output Image', img)

cv2.waitKey(0)

print(img.shape)

print("Height pixel value : ",img.shape[0])

print("Width pixel value : ",img.shape[1])
                                       
print("Number of Layers : ",img.shape[2])

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("GrayScaleImage",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

