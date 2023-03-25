# Dictionary is a collection of key-value pairs, where each key is unique and maps to a corresponding value. Dictionaries are similar to lists or arrays, but instead of using a numerical index to access elements, they use keys.
Student = {'First name': 'Rizwan shoukat',
           'Age': '19', 'Organisation': 'bytewise limited'}
# Adding n Dictionaries

Student['Age'] = 'Guess how old i am?'
# in upper we change output instead of 19 by changing key value
Student['Track'] = 'Deep learning'
# we enter new entry in dictionary


print(Student['First name'])
print(Student['Age'])
print(Student['Organisation'])
print(Student['Track'])
# if we'll try to access wrong key which we don't define than we get KEY ERROR like I enter Institute instead of Organization

print(Student.get('instiute', 'This key is not define kindly define it first'))
# In upper command if we enter wronge key which do not define in  execution we get "NONE" instead of key error.we can also print instead of NONE which we want.

del Student['Track']
# in this command we delete track key value from dectionary
print(Student.items())
#we can see pairs of key and value pairs
