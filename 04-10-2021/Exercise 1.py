tuple1 = (10, 20, 30, 40)
list1 = [11, 22, 33, 44]
dict1 = {12, 23, 34, 45}

tuple2 = tuple(list1)
tuple3 = tuple(dict1)

test1 = tuple1 + tuple2 + tuple3

print(test1)
