N, K = map(int, input().split())

MOD = 10**9 + 7

if N == 1:
    print(K)
elif N == 2:  # noqa: PLR2004
    print(K * (K - 1))
else:
    print((K * (K - 1) * pow(K - 2, N - 2, MOD)) % MOD)
