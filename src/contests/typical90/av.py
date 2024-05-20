N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

points: list[int] = []
for a, b in AB:
    points.append(b)
    points.append(a - b)

points.sort(reverse=True)
print(sum(points[:K]))
