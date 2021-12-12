class Elev():
    def __init__(self, Navn, Klasse, Penge = 1200):
        self.Navn = Navn
        self.Klasse = Klasse
        self.Penge = Penge


E1 = Elev("Mark", "2.I")
print(E1.__dict__)

E2 = Elev("Peter", "3.A", Penge = 1500)
print(E2.__dict__)
