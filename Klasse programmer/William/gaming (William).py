# Get Length of Password.
# If password should contain special characters.
# Replace Letters with number. E -> 3

#Imports
import math
import string
import random

class PasswordSettings:
    def __init__(self):
        self.length = 0
        self.specialChars = False
        self.ParseLetters = False

    def GetPassLength(self):
        while True:
            try: # Catch exceptions.
                uInput = int(input("Please enter length of password: "))
                self.length = uInput

                if(self.length < 8):
                    self.length = 8
                break

            except: #Error message.
                print("Please enter a valid number.")

    def GetSpecialChar(self): #Question.
        print("Allow Special Characters: (y/n)?")

        while True:
            uInput = input("")

            if(uInput == "y"):
                self.specialChars = True
                break

            elif (uInput == "n"):
                self.specialChars = False
                break

                #Error message.
            print("Please enter a valid answer")


    def PrintSettings(self):
        print(f"Length of password: {self.length}")
        print(f"Allow Special Characters {self.specialChars}")

    def GetSettings(self):
        self.GetPassLength()
        self.GetSpecialChar()

    def generatePassword(self):
#alphabet with all characters
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        password = ""
        while len(password)<self.length:
            lenner = math.choice[alphabet]
            lenner.append(password)
        print("Password =", password)

    def GenPass(self):
        #current char of pass
        index = 0
        output = str()

        #current selection
        cursel = string.ascii_lowercase + string.ascii_uppercase

        if(self.specialChars == True): # Special
            cursel += string.punctuation

        while True:
            #select random chararter in string of useable characters
            output += cursel[random.randint(0, len(cursel)-1)]

            index += 1
            #stop passgen
            if(index == self.length):
                break

        return output

pSets = PasswordSettings()

def main():
    pSets.GetSettings()
    pSets.PrintSettings()
    print(f"Password: {pSets.GenPass()}")

main()

input("Press 'Enter' to Close the program")
