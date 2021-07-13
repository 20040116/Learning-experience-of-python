list1 = ["apple", "banana", "orange"]
###修改列表元素
list1[0] = "watermelon"
print(list1) ###['watermelon', 'banana', 'orange']
###在列表中添加元素
#1、在末尾添加元素
list2 = []
list2.append("apple")
print(list2)
#2、在列表中插入元素、
list2.insert(0, "123") ### list2 = ['123', 'apple']
###从列表中删除数据
#1、根据位置删除数据
del list2[0]
list2.pop(0) ###list2 = []
#2、根据值删除数据
list3 = ["1", "1", "2", "3", "4", "5", "6"]
list3.remove("1") ###只能删除遇到的第一个值


###sort()对列表进行永久性排序
list3.sort(reverse=True) #反向排序
print(list3)
###sorted()是临时性的排序
print(sorted(list3)) ###注意：sorted()函数没有 .sorted()的用法
###反转列表元素顺序
list4 = ["1", "2", "3"]
list4.reverse()
###确定列表长度
len_list4 = len(list4)


###遍历整个列表
list5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for number in list5:
    print(number, end=" ") #print()函数默认输出换行
print()
#print(number)  注意：number只是临时变量
###使用list()可直接将一串数字变为列表
list6 = list(range(1,11,2)) #可以指定步长，如果最后一个数字等于则没有
print(list6)
list7 = list(range(1,11))
###进行简单的统计计算
min_list7 = min(list7)
max_list7 = max(list7)
sun_list7 = sum(list7)
###列表解析
list8 = [value**2 for value in range (1,11)]
print(list8) ###1到10的平方根


###列表切片
list9 = list(range(1,11))
a = list9[0:3]
b = list9[:4]
c = list9[2:]
###遍历切片
for number in list9[:3]:
    print(number, end=" ")
print()
###复制列表
list9_copy = list9[:]
print(list9_copy)
list9_copy.append("100")
print(list9_copy)
print(list9)  ###list9和list9_copy不同说明是两个列表
### 注意：直接赋值的方法在python中不是复制，只是把两个指针指向同一个位置



###元组——不可变的列表
example = (1, 2, 3, 4, 5)
print(example)
print(example[0])
###遍历元组的方式与列表类似
for number in example[:3]:
    print(number, end=" ")
print()
###元组无法修改其中的元素
#e.g.: example.append(1)会报错
#但是可以通过重新定义该元组改变其值
example = (6, 7, 8, 9)
print(example)


###检查特定值是否在列表里
list1 = list(range(1,11))
if (1 in list1) and (2 in list1) and (100 in list1):
    print("1 in list1")
elif (10 in list1):
    print("10 in list1")
###不包含就是 “not in”

###python中没有C++中的分支语句，如果有多个正确的判断条件，可以把这些条件放在列表里，然后判断输入条件是否在这些列表里
###在检查列表之前检查列表是否为空的很重要
#list1=[]
if list1:
    for number in list1:
        print(number, end=" ")
    print()
else:
    print("list cannot be empty")




