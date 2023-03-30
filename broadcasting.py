#broadcasting is a powerful mechanism that allows arrays of different shapes to be operated on with each other to perform mathematical operations efficiently.
#Broadcasting allows NumPy to operate on arrays of different shapes and sizes as long as they conform to certain rules.

import numpy as np
riz1=np.array([1,2,3,])
#we can see shape of an array the command for it is below
print(riz1.shape)
riz2=np.array([[7],[8],[9]])
print(riz2.shape)
print( riz1+ riz2 )

#size  of each dimension should be same
#size of one of the dimension should be 1
#