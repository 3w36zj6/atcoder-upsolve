N, K = map(int, input().split())
a = list(map(int, input().split()))

counter: dict[int, int] = {}

ans = 0

left = 0
right = 0
while left < N and right < N:
    if (len(counter) < K) or (len(counter) == K and a[right] in counter):
        if a[right] not in counter:
            counter[a[right]] = 0
        counter[a[right]] += 1

        right += 1
        ans = max(ans, right - left)
    else:
        counter[a[left]] -= 1
        if counter[a[left]] == 0:
            del counter[a[left]]
        left += 1

print(ans)
