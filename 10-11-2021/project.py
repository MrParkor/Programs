class Teacher():

    def __init__(self, Name, Class, Pay = 25000):
        self.Name = Name
        self.Pay = Pay
        self.Class = Class

T1 = Teacher("Talha", "Programmering")
print(T1.__dict__)

T2 = Teacher("Mette", "Kemi", Pay = 10000)
print(T2.__dict__)
