lo = open('Lorem.txt', 'r')
print(lo.name)
content = lo.read()
print(content)
lo.close()
#
# with open('Lorem.txt', 'r') as lo:
#     print(lo.name)
#     content=lo.readline(10)
#     print(content)
#     content=lo.readline(10)
#     print(content)
#     lo.seek(3)
#     content=lo.readline(10)
#     print(content)
#     print(lo.tell())
#
# with open('Lorem2.txt', 'r')as lo2:
#     lo2.write("YEAH!!!")
#     lo2.write(lo.read(200))
#
# with open('Timeseddel.xlsx', 'rb') as bi:
#     wer = bi.read(10)
#     print(wer)
