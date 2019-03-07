import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'ro-', label='students')
plt.plot(x1, y2, 'b^-', label='teachers')

plt.subplots_adjust(left=0.3, bottom=0.3)
plt.legend(bbox_to_anchor=(-0.15, 0.17), loc='upper right')

plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.grid(True)
plt.show()
