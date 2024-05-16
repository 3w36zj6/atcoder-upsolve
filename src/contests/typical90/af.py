import itertools

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

bad_pairs = [[False] * N for _ in range(N)]

for x, y in XY:
    bad_pairs[x - 1][y - 1] = True
    bad_pairs[y - 1][x - 1] = True

ans: int | float = float("inf")
permutations = itertools.permutations(range(N), N)
for permutation in permutations:
    total_time = 0
    for j in range(N):
        # 選手iがj区を走る
        i = permutation[j]
        if j < N - 1 and bad_pairs[i][permutation[j + 1]]:
            break
        total_time += A[i][j]
    else:
        ans = min(ans, total_time)

print(ans if ans != float("inf") else -1)
