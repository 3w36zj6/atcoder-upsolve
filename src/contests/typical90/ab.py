N = int(input())
positions = [tuple(map(int, input().split())) for _ in range(N)]

acc = [[0 for _ in range(1001)] for _ in range(1001)]

for lx, ly, rx, ry in positions:
    acc[lx][ly] += 1
    acc[rx][ry] += 1
    acc[lx][ry] -= 1
    acc[rx][ly] -= 1

for x in range(1001):
    for y in range(1000):
        acc[x][y + 1] += acc[x][y]

for x in range(1000):
    for y in range(1001):
        acc[x + 1][y] += acc[x][y]

answers = [0] * (N + 1)

for x in range(1001):
    for y in range(1001):
        answers[acc[x][y]] += 1

for ans in answers[1:]:
    print(ans)
