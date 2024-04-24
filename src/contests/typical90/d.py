H, W = map(int, input().split())
A: list[list[int]] = [list(map(int, input().split())) for _ in range(H)]

B: list[list[int]] = [[0] * W for _ in range(H)]

# 縦の和
A_vertical_sum: list[int] = [sum([A[row][col] for row in range(H)]) for col in range(W)]

# 横の和
A_horizonal_sum: list[int] = [sum(a) for a in A]

for row in range(H):
    for col in range(W):
        B[row][col] = A_vertical_sum[col] + A_horizonal_sum[row] - A[row][col]

    print(*B[row])
