set17 = input("Type the distance you want to be converted in either km or mi: ")
#Makes the input for the concertion
distance02 = int(set17)
convertion03 = set17

if convertion03.upper() == "KM":
    result = int(round(distance02 * 1.6))
    convertion02 = "Miles"
elif convertion03.upper() == "MI":
    result = int(round(distance02 / 1.6))
    convertion02 = "Kilomiters"
else:
    print("Input proper convertion")
    quit()
print("The distance in", convertion02, "is", result)
