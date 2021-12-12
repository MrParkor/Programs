print("Set in 3 numbers and I'll determain the biggest one")
#The user knows what to do
input298DB = int(input("Please input your first number (a): "))
#First input from the user
input7728 = int(input("Please input your second number (b): "))
#Second input from the user
input4EE5 = int(input("Please input your third numbber (c): "))
#Third input from the user

if(input298DB>input7728 and input298DB>input4EE5):
    print("a", "=", input298DB)
#Ser om (a) er størst, og printer det hvis det er sandt
elif(input7728>input4EE5):
    print("b", "=", input7728)
#Ser om (b) er størst og printer det hvis det er sandt
else:
    print("c", "=", input4EE5)
#Hvis hverken (a) eller (b) er størst printer den (c)
input("Press 'enter' to end program")
#Bare en linje så koden ikke lukker før man kan se svaret, og man selv kan lukke det efter
