class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = [] 
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mngr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
# print(mngr_1.email)


# mngr_1.add_employee(dev_2)
# mngr_1.print_employees()
# mngr_1.remove_employee(dev_1)
# mngr_1.print_employees()

print(isinstance(mngr_1, Developer))
print(issubclass(Manager, Employee))


# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

# print(dev_1.email)
# print(dev_1.programming_language)
