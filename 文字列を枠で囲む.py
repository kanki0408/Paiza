# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
length = len(input_line)
a = None
for i in range(length+2):
    if(a == None):
        a = "+"
    else:
        a += "+"
print(a)
print("+"+input_line+"+")
print(a)