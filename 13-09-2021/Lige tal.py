def ligetal(tal):
    if tal % 2 == 0:
        print("Ja")
    else:
        print("Nej")
ligetal(22)

def oplyft4(tal):
    x = tal * tal
    print("oplyft i 2", x)
    x = x * tal
    print("oplyft i 3", x)
    x = x * tal
    print("oplyft i 4", x)
    return x

y = oplyft4(5)
print(y)
