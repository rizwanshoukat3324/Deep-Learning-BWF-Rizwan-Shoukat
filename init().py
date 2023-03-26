#
class student:
    salary = 50000

    def __init__(self, rname, rage, rorganization):
        self.name = rname
        self.age = rage
        self.organization = rorganization

    def printdetails(self):
        return f"Name is {self.name}, age is {self.age}, and organization is {self.organization}"

Rizwan = student('Imran', '28', 'Nestle Pakistan')
print(Rizwan.name)
