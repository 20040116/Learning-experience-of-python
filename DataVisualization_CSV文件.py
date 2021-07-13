import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)  # 函数next()返回文件中的下一行，因为只调用了一次，所以返回的是第一行
    # print(header_row)
    # 获取每一列的索引和其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取某一列的值
    dates, highs = [], []
    lows = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')  # 将’-‘作为日期分割的标志
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)

# 绘制气温表

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha表示透明度
plt.plot(dates, lows, c='blue', alpha=0.5)  # 绘制第二条折线
plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.3)  # 传递一个x值和两个y值
plt.title("Daily high and low temperature of death valley - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜着的日期标签，以免它们彼此重叠
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)  # 设置刻度标记的大小

plt.savefig('Daily high and low temperature of death valley - 2014.png')
plt.show()
