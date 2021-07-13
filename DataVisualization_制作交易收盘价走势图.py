import json
import pygal
import math
from itertools import groupby


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    # a = sorted(zip(x_data, y_data))
    # print('sorted(zip(x_data, y_data)):\n', a)
    # zip()合并x_data和y_data; lamdba相当于定义了一个简单的函数， 元素’_‘相当于是任意列表
    grouped = groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0])
    # print('grouped:\n', grouped)
    for x, y in grouped:
        # print('x:\n', x)
        # print('y:\n', y)
        y_list = [v for _, v in y]
        _list = [_ for _, v in y]  # 测试得'_list'是空列表
        '''相当于：
        y_list = []
        for _, v in y:
            y_list.append(v)
        也就是'_'和'v'是两个变量，但不用'_'这个变量
        '''
        # print('_:\n', _list)
        # print('y_list\n', y_list)
        xy_map.append([x, sum(y_list) / len(y_list)])
    # print('xy_map:\n', xy_map)
    x_unique, y_mean = [*zip(*xy_map)]  # 把zip合并的分开
    # print('x_unique\n', x_unique)
    # print('y_mean\n', y_mean)
    line_charts = pygal.Line()
    line_charts.title = title
    line_charts.x_labels = x_unique
    line_charts.add(y_legend, y_mean)
    line_charts.render_to_file(title + '.svg')
    return line_charts


# 将数据加载到一个列表里
filename = 'btc_close_2017.json'
with open(filename) as f_obj:
    btc_data = json.load(f_obj)

# 打印每一天的信息
dates, months, weeks, weekdays, closes = [], [], [], [], []
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # python 不能将包含小数点的字符串转化为整数，要先转化为float
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)
    # print("{} is month {} week {}, {}, the close price is {}RMB".format(date, month, week, weekday, close))
# print(dates)
# print(months)

# 绘制收盘价月日均值
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值（￥）', '月日均值')

# 绘制收盘价周日均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值（￥）', '周日均值')

# 绘制收盘价星期均值
idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]  # 原来的周几是字符串， 这里转化为整数，防止分组排序时顺序有问题
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], "收盘价星期均值（￥）", '星期均值')
line_chart_weekday.x_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

# 绘制收盘价数据仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图（￥）.svg', '收盘价对数变换折线图（￥）.svg', '收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
    ]:
        html_file.write('<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')

# 绘制收盘价对数变换折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# x_label_rotation=20旋转20度， show_minor_x_labels=False不需要显示所有x轴标签
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]  # 用以10为底的对数函数math.log10计算收盘价。半对数（semi-logarithmic）变换
line_chart.add('收盘价', closes_log)  # 给纵坐标添加数据
line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')
