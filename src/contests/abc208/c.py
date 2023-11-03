N, K = map(int, input().split())
a = list(map(int, input().split()))

sweets = [{"i": i, "a": a[i], "sweet": K // N} for i in range(N)]
sweets.sort(key=lambda sweet: sweet["a"])

for i in range(K % N):
    sweets[i]["sweet"] += 1

sweets.sort(key=lambda sweet: sweet["i"])

for sweet in sweets:
    print(sweet["sweet"])
