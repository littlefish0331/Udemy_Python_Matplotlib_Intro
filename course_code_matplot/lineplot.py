import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

plt.plot(x1, y1, 'ro--', label='students')
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.show()
