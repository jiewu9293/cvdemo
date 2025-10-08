import cv2
#read image
#img = cv2.imread("1.jpg",0) 0 means read the img in gray mode so if we have 0 here, we don't need to convert to gray scale image at below
img = cv2.imread("1.jpg")
#convert to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#binarization
#return the image after binarization
ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #pixel <=127 will be set to 0 pixel > 127 will be set to 255, we are using thresh_binary algorithm

#show the image
cv2.imshow('gray',binary) #name of the window, and the image we show
cv2.waitKey(0) #open the window and wait until a key is entered
#purpose of binarization is highlight the foreground ignore the background