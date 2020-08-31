target = 10 ** 9 + 7

N = int(input())

# 全ての整数のリスト作成
int_list = list(input().split())
int_list = [int(n) for n in int_list]

int_sum = sum(int_list)

sum_result = 0
for num in int_list:
    int_sum -= num
    sum_result += num * int_sum
print(sum_result % target)
