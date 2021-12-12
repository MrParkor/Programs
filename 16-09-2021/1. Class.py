# #Variables
#
# #------------------------------------------------------------------------------
# #Age limit
#
# age_limit = 18
# user_age = int(input("Enter the number: "))
# #number2 = int(number2)
#
# if user_age >= age_limit:
#    print("You are welcome to enter the club")
# elif user_age < 13:
#    exit()
# else:
#    print("Entry denied!")
#
# #Age limit
# #------------------------------------------------------------------------------
#
#
# #------------------------------------------------------------------------------
# #Number converter
#
# number = 25
# print(number) # 25
# number = float(number)
# print(number) # 25.0
#
# #Number converter
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #concatonation
#
# number1 = 300
# number2 = 300
#
# print(number1 + number2)
#
# string1 = "Hello "
# string2 = "World! "
#
# print(string1 + string2)
# #print(number1 +" " + string1) # Error
# print(str(number1) +" " + string1) # Fix
#
# #concatonation
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #While Loops
#
# number1 = 0
# while number1 <5:
#     number1 = number1 + 1
#     print(number1)
# print("Loop has finished")
#
# number2 = 5
# while number2 >= 0 :
#     print(number2)
#     number2= number2 - 1
# print("Loop has finished")
#
# while True:
#     User_input = input("Enter some message: ")
#     if User_input == "Done" or User_input == "done":
#         break
#     else:
#         print(User_input)
#
# print("Loop has been broken")
#
# #While Loops
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #Lists
#
# #------------------------------------------------------------------------------
# #part 1
#
# _2i = ["Lian", "David", "Noah", "Mikkel BB", "Gustav", "Aya"]
# #       0       1       2           3           4       5
#
# print(_2i)
# print(_2i[1]) #David
# print("length of the list is ", len(_2i))
# print("List in sorted form: ", sorted(_2i))
#
# #append function for adding value to the end of the list
#
# _2i.append("Mark")
# _2i.append("Isabel")
# _2i.append("Kavin")
# _2i.append("Nikolai")
#
# print(_2i)
# print(sorted(_2i))
# print("Sliceing a list: ", _2i[1:5])
#
# #Part 1
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #Part 2
#
# _2i = [100, ["David", "Noah", "Mikkel BB", "Gustav",], "Aya", ["Mark", "Isabel"]]
# #        0       1       2           3           4       5
#
# print(_2i[0])#100
# print(_2i[1])
# print(_2i[1][0])#David
# print(_2i[3])
# print(_2i[3][1])#Isabel
#
# #Part 2
# #------------------------------------------------------------------------------
#
# #lists
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #For Loop
#
# #------------------------------------------------------------------------------
# #Part 1
#
# testlist = ["Test1", "Test2", "Test3"]
# #printing elements of lists using index numbers
# print(testlist[0],"\n")
# # printing elements of the list using for loop
# for element in testlist:
#     print(element)
#
# print("Loop has been terminated")
#
# #Part 1
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #Part 2
#
# #Using list as a variable
# shopping_list = list()
# shopping_list.append("Honey")
# shopping_list.append("Pringles")
# shopping_list.append("Bread")
# shopping_list.append("Milk")
#
# print(shopping_list)
#
# del(shopping_list[0])
#
# print(shopping_list)
#
# shopping_list.insert(2, "Chokolate")
# print(shopping_list)
#
# #Part 2
# #------------------------------------------------------------------------------
#
# #For Loop
# #------------------------------------------------------------------------------
#
# #------------------------------------------------------------------------------
# #Dictionaries
#
# student = {"Name": "Aya", "Age": 16, "Class": "2i", "Adress": "Ballerup"}
# print(student)
# student["workplace"] = "National Museum"
# print(student)
# print("Name of the student is:", student["Name"])
#
# for key in student:
#     print(key)
#
# for key, value in student.items():
#     print(key, " - ", value)
#
# print("Name" in student)
#
# #Dictionaries
# #------------------------------------------------------------------------------
