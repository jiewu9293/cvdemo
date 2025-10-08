import cv2
#blur example
#read image
img = cv2.imread("1.jpg")

#display img
cv2.imshow('original',img)

#convert img to gray scale img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#blur
blurred = cv2.blur(gray,(35,5)) #specify which img we need to blur, and a kernal size (5,5)
cv2.GaussianBlur(gray,(35,35),0) #if we want to keep more edges we need to use gaussianblue and bilateral filter
cv2.medianBlur(gray,35)
cv2.bilateralFilter


#binarization
_,thresh =cv2.threshold(blurred,135,255,cv2.THRESH_BINARY)

#dilate
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # input are type of the kernal and the size of the kernal, return the kernal
dilated = cv2.dilate(thresh,kernal,iterations=3)

#display the image after dilation
cv2.imshow('Eroded',dilated)

cv2.waitKey(0)