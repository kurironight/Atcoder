S = input()
T = input()

num_list = []

for i in range(len(S)-len(T)+1):
    num = len(T)
    for j, target in enumerate(S[i:i+len(T)]):
        if target == T[j]:
            num -= 1
    num_list.append(num)
print(min(num_list))
