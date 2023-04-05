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

# below both commands where use for getting excel sheets to pandas
# riz2=pd.read_csv('brother.csv')
# print(riz2)
path = "H:\\Deep-Learning-BWF-Rizwan-Shoukat\\task 13\\brothers.csv"
riz2 = pd.read_csv(path)
print(riz2)