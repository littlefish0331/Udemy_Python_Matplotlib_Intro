import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.bar(x1,y1)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()
