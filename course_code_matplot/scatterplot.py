import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("darkgrid")

N = 50
x1 = np.random.rand(N)
y1 = np.random.rand(N)
s1 = np.random.rand(N) * 300
x2 = np.random.rand(N)
y2 = np.random.rand(N)
s2 = np.random.rand(N) * 300

plt.scatter(x1, y1,s=s1)
plt.scatter(x2, y2,s=s2)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()
