#import this ### zen of python
###修改字符串的大小写
string1 = "li mingyang"
#首字母大写
string1.title()
#全部变为大写或小写
string1.upper()
string1.lower()
###合并字符串
string2 = "hello"
string12= string2 + ", " + string1 + "!"
print(string12.title())
###添加空白"\n","\t"
print("language:\n\tpython\n\tC++\n\tJavascript")
###删除字符串中的空白 .rstrip()右删除 .lstrip()左删除 .strip()两侧删除
Example = " he l lo "
print(Example.strip())
###数字转为字符串
number = 10
number = str(number) ###一定要赋值，否则不改变原数据
print(type(number))

