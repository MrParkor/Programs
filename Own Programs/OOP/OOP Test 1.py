### This is a program to immitate a human

import random

class Human:
    def __init__(self, firstname, lastname, age, gender, email = None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.email = self.firstname + '.' + self.lastname + '@gmail.com'

    def GetInfo(self):
        print('Full name:', self.firstname, self.lastname, '\n'
        'Age:', self.age, '\n'
        "Gender:", self.gender, '\n'
        "Email:", self.email)

class Animal(Human):
    def __init__(self, firstname, age, gender):
        super().__init__(firstname, age, gender)

    def Talk(self):
        


P1 = Human("Mark", "Toesing", 18, "Male")
P1.GetInfo()
