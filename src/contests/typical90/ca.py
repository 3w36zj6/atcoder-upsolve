H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

answer = 0

for row in range(H - 1):
    for col in range(W - 1):
        diff = B[row][col] - A[row][col]
        A[row][col] += diff
        A[row][col + 1] += diff
        A[row + 1][col] += diff
        A[row + 1][col + 1] += diff
        answer += abs(diff)

if A == B:
    print("Yes")
    print(answer)
else:
    print("No")
