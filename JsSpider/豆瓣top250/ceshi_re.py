import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))   # 不在起始位置匹配
#结果显示
# (0, 3)
# None


# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#结果显示
# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter


# pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
# m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
# print(m)
# m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
# print(m.group())
# print(m.start())
# print(m.end())
# print(m.span())
#结果显示
# None
# 12
# 3
# 5
# (3, 5)

# import re
# pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# m = pattern.match('Hello World Wide Web')
# print(m.start(2))
# print(m.span(2))
# print(m.span(0))
# print(m.group(1))
#结果显示
# 6
# (6, 11)
# (0, 11)
# Hello

# import re
#
# result1 = re.findall(r'\d+', 'runoob 123 google 456')
# pattern = re.compile(r'\d+')  # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# result3 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# print(result3)
#结果显示
# ['123', '456']
# ['123', '456']
# ['88', '12']

# import re
#
# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print(match.group())
# 结果显示
# 12
# 32
# 43
# 3

# import re
# x = re.split('\W+', ' runoob, runoob, runoob.')
# # ['runoob', 'runoob', 'runoob', '']
# print(x)
# y = re.split('(\W+)', ' runoob, runoob, runoob.')
# # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# print(y)
# z = re.split('\W+', ' runoob, runoob, runoob.',1)
# # ['', 'runoob, runoob, runoob.']
# print(z)
# w = re.split('e*', 'heello woerld')
# print(w)
# f = re.findall('[aeiou]','hauhdifahgsifeeoohdasihf')
# print(f)
