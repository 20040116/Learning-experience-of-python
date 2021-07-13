###指定默认参数的形式参数需要移到形式参数列表末尾
###一般而言，输入函数的列表会被永久修改
###为防止原列表被修改，可以如此调用函数 "function_name(list_name[:])"
###传递任意数量的实参
def example(*choices):  # 相当于创建了一个名为choices的空元组，并将所有收到的值都装到该元组里
    for choice in choices:
        print(choice)


def build_profile(**user_info):  # user_info就是一个空字典，可以接受键-值对输入
    profile = {}
    for key, value in user_info.items():
        profile[key] = value
    return profile


example("1", "2", "3")
###如果要让函数接受不同类型的实参， 必须在函数定义中将接纳任意数量实参的形参放在最后


###使用任意数量的关键字实参
flag = True
user_input = {}
while flag:
    key = input("key:")
    value = input("value:")
    user_input[key] = value
    a = input("would you want to quit? y/n")
    if a == "y":
        flag = False
    else:
        flag = True
print(user_input)
user_profile = build_profile(a="1", b="2")  # 不能直接给形参一个字典——build_profile(user_input), 输入给形参的必须是键-值对
print(user_profile)

###将函数储存在模块中
###注意：模块文件即.py文件的名称不要有括号等特殊字符
###导入整个模块："import module_name"
###导入特定函数："from module_name import function_name"
###给函数指定别名："from module_name import function_name as 别名"
###给模块指定别名："import module_name as 别名"
###导入模块中的所有函数："from module_name import *"
###如果形参过多
# def function_name(
#         parameter_0, parameter_1,
#         parameter_2, parameter_3
# ):
