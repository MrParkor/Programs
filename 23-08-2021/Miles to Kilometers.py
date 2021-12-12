print("I can convert miles to Kilometers and vice versa:\n")

temp = input("Tell me the distance you want converted (Fx 20km or 12mi): ")
Distance = int(temp[:-1-2])
i_convention = temp[-1-2]

if temp.upper() == "KM":
    result = float(round(1.6*Distance))
    o_convention = "Miles"
elif temp.upper() == "MI":
    result = float(round(Distance/1.6))
    o_convention = "Kilometers"
else:
    print("I can't understand: Try again")

print("The Distance in", o_convention, "is", result)
input("Press 'enter' to close")
