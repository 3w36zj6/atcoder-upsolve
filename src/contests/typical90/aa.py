N = int(input())
S = [input() for _ in range(N)]

users: set[str] = set()

for i in range(N):
    if S[i] not in users:
        print(i + 1)
        users.add(S[i])
