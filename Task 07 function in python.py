# A function is a block of code that performs a specific task whenever it is called.In bigger programs where we have large
# amounts of code,it is advisable to create or use existing functions that make the program flow organized and neat
# there are two types of funtion 01=built in function  02User define function
def calculate(a, b,):
    # in this defining function a and b are the parameters
    mean = (a*b)/(a+b)
    print(mean)
def greater(a, b):
    # in this defining function a and b are the parameters
    if (a < b):
        print("your values is too small")
    elif (a == b):
        print('your value is Equal')
    else:
        print('your value is greater')
def lesser(a, b):
    pass
# where pass means leave it and process next
a = 9
b = 4
greater(a, b)
mean = (a*b)/(a+b)
print(mean)
# in this defining function a and b are the Argument which is run and parameter will not be run
calculate(2, 2)
greater(2, 2)


# Docstring is a string literal that appears as the first statement in a module, function, class, or method definition. Its purpose is to document what the code does, and how it can be used.
# Docstrings can be accessed at runtime using the __doc__ attribute of the corresponding object.
def Rizwan():
    '''In below Rizwan is a function name,def is a keyword for defining'''
    # Remember one thing important which is that docstring is only written on the next line of "def function" if we write it on third line than __doc__ will show none
print('hello Rizwan')
print('Welcome to bytewise limited')
# print(Rizwan.__doc__)
help(Rizwan)
# we can use upper both commands for getting docstring output


# Arbitrary Number of Arguments
def imran(*args):
    for item in args:
        print(item)
Famlilymembersname = ['Rizwan', 'Shoukat',
                      'Shaban', 'Ramzan', 'Alishan', 'Imran']
imran(*Famlilymembersname)
# In arbitrary number of argument we put just * so that we can enter entites as we want
