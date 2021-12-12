x = int(input("Enter a number thats higher than 1: "))

while x != 1:


    if x%2 == 0:
        x = x/2
        print(int(x))

    elif x%2 != 0:
        x = x*3+1
        print(int(x))



input("Press 'Enter' to terminate the program")
