import statistics

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

x_median = statistics.median_low([x for x, _ in XY])
y_median = statistics.median_low([y for _, y in XY])

print(sum([abs(x - x_median) + abs(y - y_median) for x, y in XY]))
