#every method inside a class is adefault or instance method which passes self when ever called. to avoid this static methods are used using staticmethod decorator using this self is not passed automatically.


class Employee:
    company ="IBM"

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def printDetails(self):
        print(f"{self._name} has a salary of {self._salary}")
    @staticmethod
    def sum(a,b):
        print(a+b)
    @staticmethod
    def printCompany(cls):
        print(cls.company)

    @classmethod
    def printCompanyClass(cls):
        print(cls.company)
    @classmethod
    def updateCompany(cls, newCompany):
        cls.company = newCompany
        print(f"Company updated to {cls.company}")

E1 = Employee("Sam", 564533)
E1.printDetails()
# E1.sum(5,9) This gives error as it passed self as well being a instance method. Now to change it we will add decorator static method
E1.sum(5,9)
print(E1.company)
print(Employee.company)
Employee.company = "Google"
print(Employee.company)

# To refference a class you use class methods again decorator @classmethod is used. You could use staticmethod decorator for the below as well but need to pass class name in it.
E1.printCompany(Employee)
E1.printCompanyClass()
E1.updateCompany("Microsoft")