import cv2

img = cv2.imread("1.jpg") # we will read 1.jpg and assign to img
cv2.imshow('image',img) #image is the name of the window , img is the img we will show

#wait until a key is entered, otherwise the window will close immediately after the window is opened
 #input is the waiting time, if input is zero, means the window will be waiting until a key is entered then it will close
while 1:
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()

