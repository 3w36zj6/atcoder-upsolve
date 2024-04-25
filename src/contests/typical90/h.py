N = int(input())
S = input()

# 文字列Sの最初のi文字から何文字かを抜き出してつなげる方法のうち、それが"atcoder"のj文字まで一致するものの数
dp = [[0] * 8 for _ in range(N + 1)]

dp[0][0] = 1

MOD = 10**9 + 7

for i in range(N):
    for j in range(8):
        # 選ばないとき
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        # 選ぶとき
        if S[i] == "atcoder "[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[-1][-1])
