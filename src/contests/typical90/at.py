from collections import Counter

N = int(input())
A = [int(x) % 46 for x in input().split()]
B = [int(x) % 46 for x in input().split()]
C = [int(x) % 46 for x in input().split()]

A_counter = Counter(A)
B_counter = Counter(B)
C_counter = Counter(C)

ans = 0

for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0 and A_counter[a] and B_counter[b] and C_counter[c]:
                ans += A_counter[a] * B_counter[b] * C_counter[c]

print(ans)
