from collections import deque

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

cards: deque[int] = deque()

for t, x in queries:
    if t == 1:
        cards.append(x)
    elif t == 2:  # noqa: PLR2004
        cards.appendleft(x)
    else:
        print(cards[-x])
