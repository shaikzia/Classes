# Program from Youtube Videos - corey schafer
"""
Tut1 - Classes and Instances
"""
#Defining the class
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# Creating an instances of the class
emp1 = Employee('Muhammad', 'Faiz', 60000)
emp2 = Employee('Zairah', 'Shaik',50000)
emp3 = Employee('Muhammad', 'Saad',50000)

#Printing the email
print(emp1.email)
print(emp2.email)
print(emp3.email)

# Print the Full Name
print(emp1.fullname())
print(emp2.fullname())
print(emp3.fullname())