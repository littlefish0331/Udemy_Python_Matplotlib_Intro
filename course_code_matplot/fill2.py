import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0,10)
Y1 = 0.05*X*X
Y2 = 0.03*X*X

plt.ylim(0, 5)
plt.plot(X, Y1, color='blue')
plt.plot(X, Y2, color='red')
plt.fill_between(X, Y1, Y2, color='red', alpha='0.5')
plt.show()