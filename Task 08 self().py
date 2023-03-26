class student:
    salary = 50000
    #This is class variable if we put any attribute or entity after class acually it will assign to all like assign to imran and rizwan

    def printdetails(self):
        return f"Name is {self.name} age is {self.age} and organization is{self.organization}"
    #where self is an instance which is use for this command when we run this self automatically replace with Attribute like rizwan ,imran and student etc
rizwan = student()
Imran = student()
rizwan.name = 'Rizwan shoukat'
rizwan.age = '19'
rizwan.organization = 'Bytewise limited'
Imran.name = 'Imran Shoukat'
Imran.age = '28'
Imran.organization = 'Nestle Pakisan'
Imran.salary = '35000'
 #in upper we assign indiviually salary to imran
print(Imran.printdetails())
#when we run this it will give us statement which we write in return value and give name age and organization of Imran which we write in upper
