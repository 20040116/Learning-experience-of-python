import matplotlib.pyplot as plt
###绘制简单的折线图
input_values = [1, 2, 3, 4, 5] ###给plot()同时提供输入和输出值，以改变默认值
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)###修改线条宽度

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
