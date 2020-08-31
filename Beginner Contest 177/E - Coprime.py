def gen_d_prim(n):
    D = [0, 0] + [-1] * (n-1)
    for i in range(2, n+1, 2):
        D[i] = 2
    for i in range(3, n+1, 2):
        if D[i] > 0:
            continue
        for j in range(i, n+1, i):
            D[j] = i
    return D


def is_pairwise(A):
    D = gen_d_prim(10**6)
    past = set()
    for a in A:
        now = set()
        while a != 1:
            # 素数 D[a]: 今回は未済 & 過去で済
            if not D[a] in now and D[a] in past:
                return False
            now.add(D[a])
            past.add(D[a])
            a //= D[a]
    return True


def gcd_all(A):
    from math import gcd
    g = 0
    for a in A:
        g = gcd(g, a)
    return g


def solve():
    if is_pairwise(A):
        return 0
    if gcd_all(A) == 1:
        return 1
    return 2


n = int(input())
A = [*map(int, input().split())]
print(['pairwise', 'setwise', 'not'][solve()], 'coprime')
