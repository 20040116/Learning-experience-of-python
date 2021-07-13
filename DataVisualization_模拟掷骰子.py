import pygal
from random import randint


class Die():
    '''表示骰子的类'''

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


###投掷两个骰子
die = Die(10)
die2 = Die(6)
results1 = []
results2 = []
for roll_num in range(1000000):
    result1 = die.roll()
    result2 = die2.roll()
    results1.append(result1)
    results2.append(result2)

# 分析结果
frequencies = []
frequencies2 = []
for value in range(1, die2.num_sides + 1):
    frequency = results2.count(value)
    frequencies.append(frequency)
for value in range(1, die.num_sides + 1):
    frequency = results1.count(value)
    frequencies2.append(frequency)
# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000000 times."
hist.x_labels = list(range(1, 11))
hist.x_title = 'result'
hist.y_title = 'Frequency of Result'
hist.add('D6-two', frequencies)
hist.add('D6', frequencies2)
hist.render_to_file('die_visual_two.svg')  ###这个格式的图片需要用浏览器打开
