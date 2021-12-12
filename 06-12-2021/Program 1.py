import re
Messages = "~From: MrParkour; What were the program supposed designed for?? ~From: ThoiTool; It's a calculator"

Sender = re.findall('From: ([^;]+)', Messages)
print(Sender)

Message = re.findall('.; ([^~]*)', Messages)
print(Message)
