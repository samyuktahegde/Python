class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def Name(self):
        return self.firstname+" "+self.lastname

    def __str__(self):
        return self.firstname+" "+self.lastname+", "+str(self.age)

class Employee(Person):
    def __init__(self, first, last, age, staffnum):
        Person.__init__(self, first, last, age)
        self.staffnum = staffnum

    def getEmployee(self):
        return self.Name()+", "+self.staffnum

    def __str__(self):
        return super().__str__()+", "+self.staffnum

x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x.Name())
print(y.getEmployee())
print(x)
print(y)