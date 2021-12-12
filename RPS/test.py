#Variables to make it work
import random
from tkinter import *

root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

# Defines the pictures we use
# #-----------------------------------------------------------------------------
img = PhotoImage(file="rock.png") # 1
img2 = PhotoImage(file="paper.png") # 2
img3 = PhotoImage(file="scissor.png") # 3

# Makes the buttons
# #-----------------------------------------------------------------------------

# Defines what happens when you press the rock button
def rock():
    # Makes sure we don't hard-code stuff for the buttons
    rock = 1
    paper = 2
    scissor = 3

    # Makes sure that we get 1 value
    for i in range(1):
        # Sets a random value from 1 - 3
        value = random.randint(1, 3)
        # Tells us if we press rock and the computer got rock that it's a tie
        if value == rock:
            print("Tie")
        # Tells us if we press rock and the computer got paper that we lost
        elif value == paper:
            print("Lost")
        # Tells us if we press rock and the computer got scissor that we won
        elif value == scissor:
            print("Won")
        # Prints if theres a failure in the code
        else:
            print("Failure")

# Defines what happens when you press the paper button
def paper():
    # Makes sure we don't hard-code stuff for the buttons
    rock = 1
    paper = 2
    scissor = 3

    # Makes sure that we get 1 value
    for i in range(1):
        # Sets a random value from 1 - 3
        value = random.randint(1, 3)
        # Tells us if we press paper and the computer got rock that we won
        if value == rock:
            print("Won")
        # Tells us if we press paper and the computer got paper that it's a tie
        elif value == paper:
            print("Tie")
        # Tells us if we press paper and the computer got scissor that we lost
        elif value == scissor:
            print("Lost")
        # Prints if theres a failure in the code
        else:
            print("Failure")

# Defines what happens when you press the scissor button
def scissor():
    # Makes sure we don't hard-code stuff for the buttons
    rock = 1
    paper = 2
    scissor = 3

    # Makes sure that we get 1 value
    for i in range(1):
        # Sets a random value from 1 - 3
        value = random.randint(1, 3)
        # Tells us if we press scissor and the computer got rock that we lost
        if value == rock:
            print("Lost")
        # Tells us if we press scissor and the computer got paper that we won
        elif value == paper:
            print("Won")
        # Tells us if we press scissor and the computer got scissor that it's a tie
        elif value == scissor:
            print("Tie")
        # Prints if theres a failure in the code
        else:
            print("Failure")


# Defines the "rock" button
btn1 = Button(root, image= img, width=200, height=100, bd='10', command=rock)
# Places the button the right place
btn1.place(x=50, y=300)

# Defines the "paper" button
btn2 = Button(root, image= img2, width=200, height=100, bd='10', command=paper)
# Places the button the right place
btn2.place(x=300, y=300)

# Defines the "scissor" button
btn3 = Button(root, image= img3, width=200, height=100, bd='10', command=scissor)
# Places the button the right place
btn3.place(x=550, y=300)

# Runs the program
mainloop()
#done
