from itertools import groupby

N = int(input())
S = input()

ans = N * (N + 1) // 2
for _, group in groupby(S):
    group_len = len(list(group))
    ans -= group_len * (group_len + 1) // 2
print(ans)
