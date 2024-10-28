L, R = map(int, input().split())

answer = 0

for i in range(1, 20):
    # i桁
    min_value = max(pow(10, i - 1), L)
    max_value = min(pow(10, i) - 1, R)
    if pow(10, i - 1) <= min_value <= pow(10, i) - 1 and pow(10, i - 1) <= max_value <= pow(10, i) - 1:
        answer += i * (min_value + max_value) * (max_value - min_value + 1) // 2
        answer %= 1000000007

print(answer)
