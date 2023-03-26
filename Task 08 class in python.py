# A class is a virtual entity or a blueprint for creating objects.We can create as many objects as possible of a class
class student:
    salary = 50000
    #This is class variable if we put any attribute or entity after class acually it will assign to all like assign to imran and rizwan
    pass
rizwan = student()
Imran = student()
rizwan.name = 'Rizwan shoukat'
rizwan.age = '19'
rizwan.organization = 'Bytewise limited'
Imran.name = 'Imran Shoukat'
Imran.age = '28'
Imran.organization = 'Nestle Pakisan'
Imran.salary = '35000'
# in upper we assign indiviually salary to imran
print(rizwan.name, Imran.salary)
print(student.__dict__)
#In this command we can see the attributes of Imran,rizwan And even student Indivially

