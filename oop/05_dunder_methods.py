# Python Object Oriented Programming Dunder Methods

# class to create different individual unique employees
class Employee:
    
    # class variables
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'
        
        Employee.num_of_emps += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

# instances
emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Jamie', 'Oliver', 62000)

