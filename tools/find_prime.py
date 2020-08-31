# エラストテネスの篩

def get_sieve_of_eratosthenes(n):
    """1-n内のうち，素数を求める

    Args:
        n ([int]): 範囲を指定する

    Returns:
        [list]: 素数のリスト(1は素数でない)
    """
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


print(get_sieve_of_eratosthenes(100))
