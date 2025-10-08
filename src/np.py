import numpy as np

a = np.array([1,2,3,4,5]) #create 1d array

b = np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15]]) #2d array is matrix

#create array with all zeros
c = np.zeros((3,4)) #3 rows 4 cols
print(c)
d = np.ones((3,4)) # all ones
print(d)

e = np.eye(3)
print(e) #identity matrix

#matrix addition subtraction
f = np.array([1,2,3,4])
h = np.array([2,3,4,5])
print(f+h)

print(f-h)
print(f * h) # dot product
print(g/h)

#numpy broadcasting
i = np.array([[1,2],
              [3,4],
              [5,6]]) # 3 * 2 matrix
j = np.array([10,20]) # 1d array this array will be broadcasted to 3 * 2 matrix, the 1st row is 10,20 so as the 2nd and 3rd
print(i + j) # when we do addition, numpy will use broadcasting automatically
