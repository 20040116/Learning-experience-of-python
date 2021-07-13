import matplotlib.pyplot as plt

###手动输入值
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
###自动计算数据的一种方法
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

#plt.scatter(x_values, y_values, c='red', edgecolors='black', s=10) #'c'为点的颜色， 'edgecolors'为轮廓颜色
'''要了解pyplot中所有的颜色映射，请访问http://matplotlib.org/，单击Examples，向下滚动到Color Examples，再单击Colormaps_reference'''
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10) #使用颜色映射


plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

###设置每个坐标轴的取值范围
#plt.axis([0, 1100, 0, 1100000])

#保存图片到文件中
plt.savefig('squares_plot.png', bbox_inches='tight')###将空白的区域剪掉

plt.show()


