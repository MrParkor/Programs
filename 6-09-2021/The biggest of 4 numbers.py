print("Set in 4 numbers and I'll determain the biggest one")
#The user knows what to do

a = int(input("Please enter your first number (a): "))
#User inputs their first number:
b = int(input("Please enter your second number (b): "))
#User inputs their second number:
c = int(input("Please enter your third number (c): "))
#User inputs their third number:
d = int(input("Please enter your forth number (d): "))
#User inputs their forth number:

if(a>b and a>c and a>d):
    print("a", "=", a)
#Finder ud af om (a) er størst og printer det hvis det passer
elif(b>c and b>d):
    print("b", "=", b)
#Finder ud af om (b) er størst og printer det hvis det passer
elif(c>d):
    print("c", "=", c)
#Finder ud af om (c) er størst og printer det hvis det passer
else:
    print("d", "=", d)
#Printer d, hvis det er det største tal
input("Press 'enter' to end program")
#Bare en linje så koden ikke lukker før man kan se svaret, og man selv kan lukke det efter
