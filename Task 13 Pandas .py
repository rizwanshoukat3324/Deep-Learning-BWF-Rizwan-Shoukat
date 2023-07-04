# Pandas is an open source data analysis written in python.In leverages the power of numpy to make data analysis and pre processing
# easy for data scientites.It provides rich and highly robust data operations
import numpy as np
import pandas as pd
dict1 = {
    'Name': ['Rizwan', 'Imran', 'Ramzan', 'Shaban', 'Alishan'],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Peshawar', 'Jehlum'],
    ' Organization': ['Bytewise', 'Nestle', 'Police', 'Warden', 'Mechanic'],
    'Age': [19, 28, 26, 24, 21]
}
riz = pd.DataFrame(dict1)
print(riz)

# if we want to export like upper data in 'csv' means in excel the the below command is use.
riz.to_csv('brothers.csv')
# the below command is use when we did n't want index The below command delete index from atble
riz.to_csv('brothers_index_false.csv', index=False)

# Below command is use when we have thousands and millions of entries in our table then this is use for seeing top head entries
riz.head(3)
print(riz.head(3))

# Below command is use when we have thousands and millions of entries in our table then this is use for seeing top last entries
riz.tail(2)
print(riz.tail(2))

# this command calculate oue numatriacal values in table like Minimin value,maximun value,standard deviation,25%,50%,755 etc
riz.describe()
print(riz.describe())

# below both commands where use for getting excel sheets to pandas
# riz2=pd.read_csv('brother.csv')
# print(riz2)
path = "H:\\Deep-Learning-BWF-Rizwan-Shoukat\\task 13\\brothers.csv"
riz2 = pd.read_csv(path)
print(riz2)

# this is use for getting particular columns entries
riz2['City']
print(riz2['City'])


# this is use for getting indivitual index in given data
riz2['City'][3]
print(riz2['City'][3])

# this command is use for changing value in data set
riz2['City'][3] = 'Mehmodabad'
print(riz2)

riz2.to_csv('brothers city .csv')

# if we wnat to change index value then
riz2.index = ['first', 'second', 'third', 'fourth', 'fifth']
print(riz2)

# SERIES
ser = pd.Series(np.random.rand(34))
print(ser)
# this command is use for getting data type
type(ser)
print(type(ser))


# Dataframe
riz3 = pd.DataFrame(np.random.rand(32, 5), index=np.arange(32))
print(riz3)
print(type(riz3))

######################
riz3[0][1] = 'Rizwan'
riz3[0][2] = 'shoukat'
riz3[0][3] = 'bytewise Limited'
print(riz3)

riz3.head()
print(riz3.head())
riz3.index
print(riz3.index)
riz3.columns
print(riz3.columns)

# if we wnat to convert pandas data to numpy then we sue this command
riz3.to_numpy
print(riz3.to_numpy)
print(type(riz3.to_numpy))

# below command is use to get tranpose of given data which if we have (45,5) after this command the output will be (5,45)
riz3.T
print(riz3.T)
# Below command sort my data index from 32 to 01 instead of 01 to 31
riz3.sort_index(axis=0, ascending=False)
print(riz3.sort_index(axis=0, ascending=False))
# this command sort my data columns from 05 to 01 instaed of 01 to 05
riz3.sort_index(axis=1, ascending=False)
print(riz3.sort_index(axis=1, ascending=False))

# this command is use for creating copy of existing data frame in thsi example i create copy of riz3
riz4 = riz3.copy()
riz4[0][12] = 'Imran shoukat'
print(riz4)

riz4.columns = list("ABCDE")
