import numpy as np
Bytewise = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(Bytewise)

# for mean
Bytewise.mean()
print(Bytewise.mean())

# for cumsum
Bytewise.cumsum()
print(Bytewise.cumsum())

# for cumproduct
Bytewise.cumprod()
print(Bytewise.cumprod())

# for only sum
Bytewise.sum()
print(Bytewise.sum())

# for comperison
Bytewise > 4
print(Bytewise > 4)

# for seeing countity for true valus
Rizwan = Bytewise > 4
Rizwan.sum()
print(Rizwan.sum())

# for checking the true value. Inthis command we saying that if any single entity is true then print ture
Rizwan.any()
print(Rizwan.any())

# for checking false value
Rizwan.all()
print(Rizwan.all())

# for sorting
C = np.array([1, 5, 5, 8, 2, 8, 76, 47, 9, 2, 46, 7, 6565])
print(C)
sorted_arr = np.sort(C)
print(sorted_arr)

#for finding unique vales in list which is repeat
np.unique(C)
print(np.unique(C))
