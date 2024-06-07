from bisect import bisect_left
from itertools import accumulate

N = int(input())
A_ = list(map(int, input().split()))
A = A_[:] + A_[:]

A_acc = list(accumulate(A))

for a_left in A_acc:
    bisect_index_left = bisect_left(A_acc, a_left + A_acc[N - 1] // 10)
    if (0 <= bisect_index_left <= (N - 1) * 2) and A_acc[bisect_index_left] * 10 == a_left * 10 + A_acc[N - 1]:
        print("Yes")
        break
else:
    print("No")
