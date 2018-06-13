# Program from Youtube Videos - corey schafer
"""
Tut2 - Class Variables - Variables that are shared among all instances of the class
"""
class Employee():
    num_of_emps = 0
    raise_amount = 1.04  # This is a Class Variable
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Sajida','Begum',60000)
emp2 = Employee('Mohammed','Zia',70000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

Employee.raise_amount = 1.05
emp1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

print(Employee.num_of_emps)