import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0,10)
Y1 = 0.05*X*X

plt.ylim(0, 5)
plt.plot(X, Y1, color='blue')
plt.fill_between(X, Y1, color='red', alpha='0.5')
plt.show()
