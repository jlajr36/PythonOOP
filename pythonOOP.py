#Python Object-Oriented Programming

class Employee:
    raise_amount = 1.04

    #Constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Joe','Brown',6000)
emp_2 = Employee('Steve','North',4500)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.06

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)