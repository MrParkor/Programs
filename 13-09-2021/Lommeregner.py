
def Gange(x,y):
    return x * y

def Divider(x,y):
    return x / y

def Minus(x,y):
    return x - y

def Plus(x,y):
    return x + y

do = input("Hvad vil du?: ")
x = int(input("Please enter your first number: "))
y = int(input("Please enter your second number: "))

if do == "Plus":
    print(Plus(x,y))
elif do == "Minus":
    print(Minus(x,y))
elif do == "Divider":
    print(Divider(x,y))
elif do == "Gange":
    print(Gange(x,y))
else:
    print("Jeg forstår ikke")
