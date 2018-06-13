# Program from Youtube Videos - corey schafer
"""
Tut4 - Static Methods - Methods which does not need a Class or Instance of a Class
to execute and give result
"""
import datetime

class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_day = datetime.datetime(2018,6,16)
emp1 = Employee.is_workday(my_day)
print(emp1)