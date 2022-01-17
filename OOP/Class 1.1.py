class Person:
    def __init__(self, FirstName, LastName, HairColor, Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.HairColor = HairColor
        print(self.__dict__)

class Teacher(Person):
    def __init__(self, FirstName, LastName, HairColor, Salary):
        super(FirstName, LastName, HairColor)
        self.Salary = Salary

class Student(Person):
    x = 0
    def __init__(self, FirstName, LastName, HairColor, Age, Number):
        super().__init__(FirstName, LastName, HairColor, Age)
        self.Number = Number
        Number = N

        
S1 = Student("Mark", "T", "brown", "18", "15")
