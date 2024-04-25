import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B: list[int] = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    left_index = bisect.bisect_left(A, b)
    if 0 < left_index < N:
        print(min(abs(A[left_index - 1] - b), abs(A[left_index] - b)))
    elif left_index == 0:
        print(abs(A[left_index] - b))
    else:
        print(abs(A[left_index - 1] - b))
