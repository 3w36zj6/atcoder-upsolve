N = int(input())
A, B, C = map(int, input().split())

ans = float("inf")

for i in range(10000):
    for j in range(10000 - i):
        v = N - A * i - B * j
        if (v % C) == 0 and v >= 0:
            ans = min(ans, i + j + v // C)

print(ans)
