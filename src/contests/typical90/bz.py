N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]

graph: list[list[int]] = [[] for _ in range(N)]

for a, b in ab:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = 0
for i in range(N):
    nodes = graph[i]
    if len(list(filter(lambda node: node < i, nodes))) == 1:
        ans += 1
print(ans)
