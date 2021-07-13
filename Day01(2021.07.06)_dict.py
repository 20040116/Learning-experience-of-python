from collections import OrderedDict ###记录添加键-对值顺序的字典
###定义一个字典(键-值对)
#创建空字典 dict = dict{}
dict1 = {"苹果": "apple", "香蕉": "banana", "橙子": "orange"}
print(dict1)
#返回与键相关联的值
print(dict1["苹果"])
###添加键-值对
dict1["西瓜"] = "watermelon"
dict1["芒果"] = "mango"
print(dict1)
###修改字典中的值
dict1["芒果"] = "mangguo"
print(dict1)


###删除键-值对
del dict1["芒果"]
print(dict1)
###字典的另一种书写形式
# dict1 = {"苹果": "apple",
#          "香蕉": "banana",
#          "橙子": "orange"
#          }

###遍历字典
for key, value in dict1.items(): #items()返回一个包含key和value的列表
    print(key, end=": ")
    print(value)
###注意：键-对值的返回顺序通常与储存顺序不同
###遍历字典中的所有键 .keys()
for key in dict1.keys(): #.keys()返回一个包含所有key的列表
    print(key, end=" ")
print()
# for key in dict1:
#     print(key, end=" ")
# print()  #与上面代码的结果一致，遍历字典默认遍历的是key值
###对返回的键进行排序
for key in sorted(dict1.keys()):
    print(key, end=" ")
print()
###遍历字典中所有的值
dict1["xigua"] = "watermelon"
for value in dict1.values(): #.values()返回一个包含所有value的列表
    print(value, end=" ")
print()
###此种方法无法剔除字典中重复的Value
###采用"集合——没有重复元素的列表" set()
for value in sorted(set(dict1.values())): #.values()返回一个包含所有value的列表 set()剔除重复的元素 sorted进行排序
    print(value, end=" ")
print()



###嵌套
###1、字典列表
dict1 = {"1": "apple", "2": "banana", "3": "orange"}
dict2 = {"4": "dog", "5": "horse", "6": "cat"}
dict3 = {"7": "computer", "8": "pad", "9": "phone"}
list1 = [dict1, dict2, dict3]
for dict in list1:
    print(dict)
###2、在字典中存储列表
dict1["3"] = ["orange", "橙子", "橘子"]
print(list1)
###3、在字典中嵌套字典（不例举）


###记录键-对值顺序的字典
dict4 = OrderedDict()
dict5 = {}   ###实验之后发现普通字典好像也没有打乱顺序
flag = True
while flag:
    key = input("Please input the key: ")
    value = input("Please input the value: ")
    dict4[key] = value
    dict5[key] = value
    tmp = input("Would you want to continue? y/n")
    if tmp == 'y':
        flag = True
    elif tmp == 'n':
        flag = False
for key, value in dict4.items():
    print(key, ': ',value)
print("----------------------------------------------------------------")
for key, value in dict5.items():
    print(key, ': ',value)