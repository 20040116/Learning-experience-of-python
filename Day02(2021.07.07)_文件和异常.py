###函数open()返回一个表示文件的对象
###在windows系统中，绝对路径使用‘\’而不是‘/’
file_path = 'pi_million_digits.txt'
with open(file_path) as file_object:
    ###逐行读取
    lines = file_object.readlines()  ###创建一个包含各行内容的列表
    ###读取全部内容
    contents = file_object.read()  # 此时contents为空，因为文件内容已经被lines读取
with open(file_path) as file_object:
    contents = file_object.read()

pi_string = ''
for line in lines:
    pi_string += line.strip()
if '0116' in pi_string:  ###python可以直接判断一段字符串是否在另一段字符串里
    print('yes')
else:
    print('no')
### pi_string.replace('14', '23') .replace()函数可以直接实现替换
print(pi_string[:52] + "...")
print(len(pi_string))

###写入空文件
###读取模式（“r”）、写入模式（“w”）、附加模式（“a”）、同时读取和写入（“r+”）
with open('programming_learning1.txt', 'w') as file_learning:  ###'w'模式会覆盖原来的内容，相当于重新写入
    file_learning.write("This is a test.\n")
    file_learning.write('Another test.\n')

###异常处理
###1、处理ZeroDvisionError异常
# a = int(input("Please input a: "))
# b = int(input("Please input b: "))
try:
    answer = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

else:
    print(answer)
###2、处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist!")
    pass  ###如果出现错误什么都不说

else:
    words = contents.split()  ###以空格为分隔符将字符拆分成多个部分
    num_words = len(words)
    # print(words)
    print("《Alice》 has " + str(num_words) + " words")

###存储数据
import json

numbers = list(range(0,11))
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)  ###保留python中的原格式
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)  ###将保留的原格式数据读取出来
