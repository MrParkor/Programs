#First we import the random module, which allows us to generate pseudo-random numbers, that are based on the milliseconds passed since 1. january, 1970.
import random
#Here we open the file that we use to pull Inspirational quotes from, with an encoding argument to allow the program to read the text.
Filename = open(r"Inspirational.txt", encoding="latin1")

#Here we simplfy the variable Filename into "f"
f = Filename
#Here we establish the variable "content", which is based off the text that the program can read off the file that was opened earlier.
content = f.read()
#Here we use a function to split the text from the variables by line/paragraphs from the document.
content.splitlines()

#Makes a list and imports the contents of the file into the list. Also seperates the text into different paragraphs when it meets "--"
content_list = []
content_list = content.split("--")

#Using the import random, prints a random quote from the list - content_list
print(random.choice(content_list))

#Closes the file after it has been used
f.close()

input()
