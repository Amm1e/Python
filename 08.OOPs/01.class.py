#Class
class Employee:
    Company = "IBM"

    def getSalary(self):
        return 75000
    #self it the object which calls. Below self is emp1 andemp2
    # Self in mandatory when method made inside a class. 
#object1    
emp1 = Employee()
print(emp1.getSalary())#using function using object
print(emp1.Company)