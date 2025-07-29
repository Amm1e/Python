# these methods are used to improvise on existing functionality D= double under= underscore

class Student:
    def __init__(self, name, clas):
        self._name=name
        self._clas=clas
    
    def __str__(self):
        return f"{self._name} is in class {self._clas}"

    def __repr__(self):
        return f"name: {self._name}  clas:{self._clas}"
    
    def __len__(self):
        return len(self._name)
    
s1 = Student("Harshit", 9)
print(str(s1))
print(repr(s1))
print(len(s1))