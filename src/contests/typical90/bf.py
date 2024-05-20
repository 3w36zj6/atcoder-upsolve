N, K = map(int, input().split())

visited: list[bool] = [False for _ in range(10**5)]
history: list[int] = []
cycle: list[int] = []
cycle_start_index = -1

x = N
visited[x] = True
history.append(x)
for _ in range(K):
    y = sum(list(map(int, str(x))))
    z = (x + y) % (10**5)
    x = z
    if visited[x]:
        cycle_start_index = history.index(x)
        cycle = history[cycle_start_index:]
        print(cycle[(K - cycle_start_index) % len(cycle)])
        break
    else:
        visited[x] = True
        history.append(x)
else:
    print(history[-1])
