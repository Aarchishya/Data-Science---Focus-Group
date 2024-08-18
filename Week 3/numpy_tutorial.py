import numpy as np

# Python list
python_list = [1, 2, 3, 4, 5]
# NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])

print(type(python_list))  # Output: <class 'list'>
print(type(numpy_array))  # Output: <class 'numpy.ndarray'>

# Creating arrays
array_from_list = np.array([10, 20, 30])
zeros_array = np.zeros((3, 4))  # 3x4 array of zeros
ones_array = np.ones((2, 3))    # 2x3 array of ones
range_array = np.arange(0, 10, 2)  # Array with values [0, 2, 4, 6, 8]
linspace_array = np.linspace(0, 1, 5)  # 5 equally spaced numbers between 0 and 1

print(array_from_list)
print(zeros_array)
print(ones_array)
print(range_array)
print(linspace_array)

arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])   # Output: 10
print(arr[-1])  # Output: 50

# Slicing
print(arr[1:4])  # Output: [20 30 40]
print(arr[::2])  # Output: [10 30 50] (every second element)

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape
reshaped = arr.reshape(3, 2)
print(reshaped)

# Flatten
flattened = arr.flatten()
print(flattened)

# Ravel
raveled = arr.ravel()
print(raveled)

# Broadcasting
arr = np.array([1, 2, 3])
broadcasted = arr + 10  # Add 10 to each element

print(broadcasted)  # Output: [11 12 13]

# Basic Maths
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations
print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 * arr2)  # Output: [ 4 10 18]
print(arr1 / arr2)  # Output: [0.25 0.4  0.5 ]

# Aggregate Functions

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))  # Output: 150
print(np.mean(arr))  # Output: 30.0
print(np.std(arr))  # Output: 14.142135623730951
print(np.min(arr))  # Output: 10
print(np.max(arr))  # Output: 50
print(np.argmax(arr))  # Output: 4

# Linear Algebra
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
product = np.dot(matrix1, matrix2)
print(product)

# Transpose
transpose = matrix1.T
print(transpose)

# Determinant
determinant = np.linalg.det(matrix1)
print(determinant)

# Inverse
inverse = np.linalg.inv(matrix1)
print(inverse)




