# 入力処理
N = int(input())
input_line = list(input().split())
input_line = [int(n) for n in input_line]

ok_list = []

# 7日間の内，条件を満たしているところを抽出している
for i in range(N-7+1):
    if sum(input_line[i:i+7]) <= 5:
        ok_list.append(1)
    else:
        ok_list.append(0)

# 最大出勤日を求める
max = 0  # 最大出勤日
num = 6
for j in ok_list:
    if j == 1:
        num += 1
        if num > max:
            max = num
    else:
        num = 6

print(max)
