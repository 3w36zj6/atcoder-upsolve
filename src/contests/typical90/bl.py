N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

diff_costs = [A[i] - A[i - 1] for i in range(1, N)]
cost: int = sum([abs(diff) for diff in diff_costs])

for L, R, V in queries:
    if L - 1 - 1 >= 0:
        cost -= abs(diff_costs[L - 1 - 1])
        diff_costs[L - 1 - 1] += V
        cost += abs(diff_costs[L - 1 - 1])
    if R - 1 < N - 1:
        cost -= abs(diff_costs[R - 1])
        diff_costs[R - 1] -= V
        cost += abs(diff_costs[R - 1])

    print(cost)
