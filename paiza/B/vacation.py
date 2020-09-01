import numpy as np

input_line = list(input().split())
input_line = [int(n) for n in input_line]

N, M = input_line[0], input_line[1]

day_list = []
for i in range(N):
    day_list.append(input())

day_list = [0 if i == 'work' else 1 for i in day_list]

day_list = np.array(day_list)

index = np.where(day_list == 0)[0]
max = 0
for i in range(len(index)-M+1):
    num = 0
    day = day_list.copy()
    day[index[i:i+M]] = 1
    for j in day:
        if j == 1:
            num += 1
            if num > max:
                max = num
        else:
            num = 0

print(max)
