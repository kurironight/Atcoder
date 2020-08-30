input_line = list(input().split())
input_line = [int(n) for n in input_line]

[D, T, S] = input_line
condition = D <= T*S
if condition:
    print("Yes")
else:
    print("No")
