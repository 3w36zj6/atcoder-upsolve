from collections import Counter
from functools import lru_cache
from math import gcd

N = int(input())


def pollard_rho(n: int) -> int:  # noqa: C901
    """Pollard's rho法

    nの素因数の1つを探索する。nが素数の場合はnを返す。

    Args:
        n (int):
            素因数分解する整数

    Returns:
        int:
            nの約数

    Examples:
        >>> pollard_rho(12)
        2
        >>> pollard_rho(13)
        13

    """
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p in (1, n - 1) or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p**2) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i**2 + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x**2 + 1) % n, (y**2 + 1) % n
                    y = (y**2 + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@lru_cache(maxsize=1000)
def calculate_prime_factors(n: int) -> Counter[int]:
    """素因数分解

    nの素因数分解の結果をCounterで返す。

    Args:
        n (int):
            素因数分解する整数

    Returns:
        Counter[int]:
            素因数分解の結果のCounter

    Examples:
        >>> prime_factors(12)
        Counter({2: 2, 3: 1})

    """
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else calculate_prime_factors(f) + calculate_prime_factors(n // f)


factors = calculate_prime_factors(N)
factor_count = sum(factors.values())

if factor_count == 1:
    print(0)
else:
    for i in range(10**6):
        if factor_count <= 2 ** (i + 1):
            print(i + 1)
            break
