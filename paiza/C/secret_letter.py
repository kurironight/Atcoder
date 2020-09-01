# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
input_line = list(input())
for i in range(len(input_line)):
    if i % 2 == 0:
        input_line[i] = chr((ord(input_line[i])-N-65+26) % 26+65)
    else:
        input_line[i] = chr((ord(input_line[i])+N-65+26) % 26+65)
print("".join(input_line))
