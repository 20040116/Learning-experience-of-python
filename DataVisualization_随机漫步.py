from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    '''生成随机漫步数据的类'''

    def __init__(self, num_points):
        self.num_points = num_points

        # 漫步始于（0, 0）点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 漫步到指定距离
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1, 1])  # 选择前进方向 向左/向右
            x_distance = choice([0, 1, 2, 3, 4])  # 选择前进距离
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])  # 选择前进方向 向左/向右
            y_distance = choice([0, 1, 2, 3, 4])  # 选择前进距离
            y_step = y_direction * y_distance

            # 防止原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# 创建一个RandomWalk实例，并将其包含的点都绘制出来
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    #设置绘图窗口尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors='none', s=30)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Continue? y/n")
    if keep_running == 'n':
        break
