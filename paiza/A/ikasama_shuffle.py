# 解法が分かっていない

N = int(input())
target = list(input().split())
target = [int(n) for n in target]

S = int(input())
tool_list = []
for i in range(S):
    tool = list(input().split())
    tool = [int(n) for n in tool]
    tool_list.append(tool)

state_list = []


def montecalro(current_list, tool_list, iteration, target, next_list):
    for tool in tool_list:
        next = [current_list[i] for i in tool]
        if next == target:
            return iteration
        next_list.append(next)
    return next_list


current_list = [list(range(N))]
flag = False
for i in range(N):
    next_list = []
    for current in current_list:
        next_list = montecalro(current, tool_list, i+1, target, next_list)
        if isinstance(next_list, int):
            print(next_list)
            flag = True
            break
    current_list = next_list
    if flag:
        break
    if i == N-1:
        print(-1)
