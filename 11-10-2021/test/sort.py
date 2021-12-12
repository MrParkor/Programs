fname = input("Enter file: ")
if len(fname) < 1 : fname = "Test.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # print("**",w, di.get(w,-99))

        # if the kwy is not there count is zero
        # oldcount = di.get(w,0)
        # print(w,"old",oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w,"New", newcount)
        if len(w) >= 5:
            di[w] = di.get(w,0) + 1
        else:
            pass

        # print(w, "new", di[w])

        # if w in di:
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1
        # print(w, di[w])
        pass
# print(di)

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5]:
    print(k,v)

#
# largest = -1
# theword = None
# for k,v in di.items():
#     # print(k,v)
#     if v > largest:
#         largest = v
#         theword = k

# print(theword, largest)
