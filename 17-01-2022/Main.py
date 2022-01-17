import matplotlib.pyplot as plt
import numpy as np

data = [20, 35, 30, 35, 27]

plac = np.arange(len(data))

width = 0.35

plt.bar(plac, data, width)

plt.ylabel('Scores')
plt.xlabel("x")
plt.title("Title")
plt.show()
