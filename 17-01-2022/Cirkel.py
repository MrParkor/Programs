import matplotlib.pyplot as plt
import numpy as np

name = ['Hund', 'Kat', 'Gris', 'Hest']

number = [10, 20, 30, 40]

plt.pie(number, labels=name
    ,autopct='%1.1f%%'
    # ,startangle = 75
    # ,explode = (0.1, 0.1, 0.1, 0.1)
    )

plt.title("Dyr")
# plt.legend()
plt.show()
