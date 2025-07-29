class Animal:
    def __init__(self, name):
        self.name=name
    
    def sound(self):
        print("Generic Animal voice.....")

class Dog(Animal):
    def sound(self):
        super().sound()
        print(f"{self.name} wofff......")
    

a=Dog("Bruno")
a.sound()
print(a.name)
    
