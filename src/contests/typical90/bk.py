from collections import Counter
from itertools import product

H, W = map(int, input().split())
P: list[list[int | None]] = [list(map(int, input().split())) for _ in range(H)]

ans = 0

for bits in product([0, 1], repeat=H):
    row: list[int | None] | None = None
    row_count = bits.count(1)
    for r in range(H):
        if bits[r] == 1:
            if row is None:  # noqa: SIM108
                row = P[r][:]
            else:
                row = [row[c] if row[c] == P[r][c] else None for c in range(W)]
    if row is None:
        continue

    row = list(filter(lambda x: x is not None, row))
    if len(row) == 0:
        continue
    counter = Counter(row)
    ans = max(ans, counter.most_common()[0][1] * row_count)

print(ans)
