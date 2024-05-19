N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

shift_count = 0
for T, x, y in queries:
    if T == 1:
        A[(x - 1 - shift_count) % N], A[(y - 1 - shift_count) % N] = (
            A[(y - 1 - shift_count) % N],
            A[(x - 1 - shift_count) % N],
        )
    elif T == 2:  # noqa: PLR2004
        shift_count += 1
    else:
        print(A[(x - 1 - shift_count) % N])
