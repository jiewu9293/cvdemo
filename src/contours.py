import cv2

img = cv2.imread("1.jpg")
#rgb image has 3 channels
#gray scale image only has one channel
# convert to single chanel
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

#find contours
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#draw contours
cv2.drawContours(img,contours,-1,(0,0,255),1) # -1 means draw all the contours in the contours,thickness is 1


#calculate area of contour and length of the contour
#area = cv2.contourArea(contours[0])

#calculate the perimeter of the contour
len = cv2.arcLength(contours[0],False)
print("len = %d"%(len))


#print("area = %d"%(area))
cv2.imshow('contours',img)
cv2.waitKey(0)