class Student():
    def __init__(self, FirstName, LastName, HairColor):
        self.FirstName = FirstName
        self.LastName = LastName
        self.HairColor = HairColor
        print(self.__dict__)





class Teacher():
    def __init__(self, Name, Class):
        self.Name = Name
        self.Class = Class
        print(self.__dict__)




Talha = Teacher("Talha", "2.I")
print()

Anton = Student("Anton", "Thejsen", "Brown")
Aya = Student("Aya", "Bruun", "Blond")
David = Student("David", "Hoppe", "Brown")
Gustav = Student("Gustav", "Larsen", "?")
Isabel = Student("Isabel", "Thorsen", "half-Blond")
Kavin = Student("Kavin", "Lund", "Brown")
Lian = Student("Lian", "Kazimi", "Black")
Mark = Student("Mark", "Toesing", "Half-blond")
Mikkel_BB = Student("Mikkel", "Berthelsen", "Ginger")
Mikkel_Toft = Student("Mikkel", "Ottosen", "Brown")
Nikolai = Student("Nikolai", "Lynge", "Half-blond")
Noah_T = Student("Noah", "Thomasen", "Blond")
Noah_Jax = Student("Noah", "Haastrup", "Brown")
Robin = Student("Robin", "Noerby", "Brown")
William = Student("William", "Engeborg", "Brown")
print()
