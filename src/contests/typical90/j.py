import itertools

N = int(input())
CP = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]

C1_P = [cp[1] if cp[0] == 1 else 0 for cp in CP]
C2_P = [cp[1] if cp[0] == 2 else 0 for cp in CP]  # noqa: PLR2004

C1_P_cumsum = [0, *list(itertools.accumulate(C1_P))]
C2_P_cumsum = [0, *list(itertools.accumulate(C2_P))]

for l, r in LR:  # noqa: E741
    print(C1_P_cumsum[r] - C1_P_cumsum[l - 1], C2_P_cumsum[r] - C2_P_cumsum[l - 1])
