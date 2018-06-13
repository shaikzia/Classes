# Program from Youtube Videos - corey schafer
"""
Tut3 - Class Methods
"""
class Employee:
    hike = 1.06
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.hike)

    @classmethod  # This is a Class Method used to set the value for Class Variable
    def set_raise_amt(cls,amount):
        cls.hike = amount

    @classmethod   #using class Method as an alternative Constructor
    def from_string(cls, emp_str):
        firstn,lastn,pay = emp_str.split('-')
        return cls(firstn,lastn,pay)

emp1 = Employee('Habeeba','Banu',55000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(Employee.hike)      # Class Variable hike value before applying set_raise_amt
emp1.set_raise_amt(1.08)  # applying the Class Method and changing the Class Variable value
print(Employee.hike)      # Class Variable hike value after applying set_raise_amt
print(emp1.hike)

emp_str1 = 'Jaffer-Shaik-60000'
new_emp1 = Employee.from_string(emp_str1)
print(new_emp1.first)
print(new_emp1.last)
print(new_emp1.email)