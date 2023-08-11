import numpy as np

#Read Evaluate Print Loop - REPL

#integers = np.array([1,2,3])

#print(type(integers))
#print(integers)

#LIST COMPREHENSION
#create a one-dimensional array from a list comprehension that produces even integers form 2 through 20

#integers = np.array([x for x in range(2,21,2)])


integers = np.array([[1,2,3],[4,5,8]])

#print(integers)

#print(integers.dtype)   # determine the array's element type

#print(integers.ndim)    # determine the number of dimensions

#print(integers.shape)   # tuple showing the dimensions of the array

#print(integers.size)    # total number of elements

#print(integers.itemsize)    #number of bytes required to store each element

for row in integers:
    print(row)
    print()
    for column in row:
        print(column, end=' ')
    print()

for i in integers.flat:    # iterates through all values disregarding columns and rows
    print(i)

#print(np.zeros(5))      # create an array of 5 elements of zeors (by default float type)

#print(np.ones(5))       # create an array of 5 elements of 1s (by default float type)

#print(np.ones((2,4), dtype=int))    #create an array of 2 by 4 of ones of type int

#print(np.full((3,5),13))    #create an array of 3 row of 5 columns of the number 13

#print(np.arange(5))         # like the range function, using integers

#print(np.arange(5,10))      # includes lower limit but not upper limit

#print(np.arange(10,1,-2))   #step value for descending order


#You can produce evenly spaced floating-point ranges with NumPy’s linspace function. 
# The function’s first two arguments specify the starting and ending values in the range, 
# and the ending value is included in the array. The optional keyword argument num specifies 
# the number of evenly spaced values to produce—this argument’s default value is 50:


#print(np.linspace(0.0, 1.0, num=5))     #evenly spaced float range


'''

array1 = np.arange(1,21)        # reshape method can change the dimension 

array2 = array1.reshape(4,5)    # has to have the same number of ELEMENTS

#print(array1)

#print(array2)

#When displaying large arrays, NumPy drops the mddle rows and columns

array3 = np.arange(1,100001).reshape(4,25000)

#print(array3)

array4 = np.arange(1,100001).reshape(100,1000)

#print(array4)


numbers = np.arange(1, 6)

numbers * 2
#same as 
2 * numbers

numbers ** 3

# numbers is unchanged by the arithmetic operators
print(numbers)


#Augmented assignments modify every element in the left operand.
numbers += 10


#Broadcasting

#Normally, the arithmetic operations require as operands two arrays of the same size and shape. 
# When one operand is a single value, called a scalar, NumPy performs the element-wise 
# calculations as if the scalar were an array of the same shape as the other operand, 
# but with the scalar value in all its elements. 

numbers * [2, 2, 2, 2, 2]

# multiplying integer arrays with floating pt arrays (result is floating pt)
numbers2 = np.linspace(1.1, 5.5, 5)

print(numbers2)

numbers * numbers2

#Comparing arrays

#You can compare arrays with individual values and with other arrays. 
# Comparisons are performed element-wise. Such comparisons produce arrays of 
# Boolean values in which each element’s True or False value indicates the comparison result:


numbers >= 13

numbers2 < numbers

numbers == numbers2

'''


























 

