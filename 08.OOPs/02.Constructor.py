class Employee:

    def __init__(self, name, company, salary, experience):
        self.name=name
        self.company=company
        self.salary=salary
        self.experience=experience

    def getInfo(self):
        print(f"{self.name} works at {self.company} at a salary of {self.salary} with an experience of {self.experience} years.")

emp1 = Employee("Ammie", "Google", "2Cr", 3)
emp1.getInfo()


emp2 = Employee("Satya", "Microsoft", "2Cr", 3)
emp2.getInfo()
 
 