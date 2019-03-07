import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

colors = [ 'green', 'red', 'blue', 'orange', 'lightblue']

plt.bar(x1,y1,edgecolor='black',color=colors, linewidth=2)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()
