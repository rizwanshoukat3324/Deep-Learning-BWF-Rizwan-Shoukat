# NumPy is a Python library for numerical computing. It provides high-performance multidimensional array objects and tools for working with these arrays.
import numpy as np
# upper 'np' is short form of numpy we can write both like "import numpy" and 'import numpy as np'

# creating simple Array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# upper is an example of one dimenstional array
print(array)

# zero dimenstion array
zero_dim = np.array(186538627654275878)
print(zero_dim)

# one dimenstional array
one_dim = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(one_dim)

# two dimenstional array
two_dim = np.array([[9, 8, 7], [3, 2, 1]])
print(two_dim)

# three dimenstioanl array
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim)

# Finding dimenstion of given array
print(three_dim.ndim)  # this prints the dimenstion of given array


