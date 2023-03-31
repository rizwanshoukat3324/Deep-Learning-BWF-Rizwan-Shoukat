import numpy as np
riz = np.array([[1, 2], [3, 4]])
riz1 = np.array([[7, 5], [6, 9]])
print(riz)
# linear algebra determinant
np.linalg.det(riz)
print(np.linalg.det(riz))

# linear algebra inverse
np.linalg.inv(riz)
print(np.linalg.inv(riz))

# for transpose of a matrix
riz.transpose()
print(riz.transpose())

# for trace
np.trace(riz)
print(np.trace(riz))

riz*riz1
print(riz*riz1)

riz.shape
print(riz.shape)

#for matrix mutiplication
riz.dot(riz1)
print(riz.dot(riz1))

