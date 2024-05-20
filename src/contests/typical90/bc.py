import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for combination in itertools.combinations(A, 5):
    if (combination[0] * combination[1] % P * combination[2] % P * combination[3] % P * combination[4]) % P == Q:
        ans += 1

print(ans)
