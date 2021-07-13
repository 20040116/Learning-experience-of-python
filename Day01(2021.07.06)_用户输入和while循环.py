###一种创建多行字符串的方式
question = "If you tell us who you are, we can personalize the message you see?"
question += "\nWhat's your name? "
# name = input(question) #变量可以传递给input()函数
# print("\nHello " + name +"!")
###输入的都为字符串，用int()来获取数字输入


###用while循环来处理列表和字典
###1、删除包含特定值的所有列表元素
list1 = [1, 2, 3, 4, 5, 5, 6, 7, 5, 8, 6, 5]
#list1 = set(list1)
while 5 in list1:
    list1.remove(5)
print(list1)
###2、使用用户输入来填充字典
responses ={}
flag = True
while flag:
    list = []
    name = input("What's your name?" )
    response = input("Would you like to join us ? y/n ")
    if response == "y":
        answer = input("When would you have the time to come ? ")
        list = [response, answer]
    else:
        list = [response]
    responses[name] = list
    repeat = input("Would like to welcome the next ? y/n ")
    if repeat == "y":
        flag = True
    else:
        flag = False
print(responses)
for name, list in responses.items():
    print(name+":")
    for answer in list:
        print(answer)
