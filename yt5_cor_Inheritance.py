# Program from Youtube Videos - corey schafer
"""
Tut5- Inheritance
"""
class Employee:
    hike = 1.10
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first ,self.last)

# Create a Sub Class - Developer
class Developer(Employee):
    pass

dev_1 = Employee('Hashir', 'Aayan', 55000)
dev_2 = Employee('Muhammad', 'Amaan', 56000)

# Printing full name and email
print(dev_1.fullname())
print(dev_1.email)
print(dev_2.fullname())
print(dev_2.email)
print(help(Developer))