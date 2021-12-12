mail = str(input("Please enter an Email and I'll give you the domain: ") + " ")

pos1 = mail.find("@")
print(pos1)

pos2 = mail.find(" ", pos1)
print(pos2)

host = mail[pos1+1 :pos2]
print(host)
