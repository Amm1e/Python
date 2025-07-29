class Employe:

    def __init__(self, name, salary):
# using _ as a prefix for the internal name as it makes confusion for the interperetter to know wich name to call as name is being changed.
        self._name = name
        self.salary = salary
    @property
    def firstName(self):
        l=self._name.split(" ")
        print(f"{l[0]} is first name.")
    @firstName.setter
    def firstName(self, first):
        l = self._name.split(" ")
        l[0] = first
        print(f"{first } is set as first name")
        newName = f"{first} {l[1]}"
        self._name=newName
    @property
    def name(self):
        print(f"The name is {self._name}")
e = Employe("Hello World", 3333333);
e.name
e.firstName
e.firstName ="Beautiful"
e.name
