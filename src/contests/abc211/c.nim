let S = readLine(stdin)

const MOD = int(1e9) + 7
const CHOKUDAI = "chokudai"

var dp: seq[seq[int]] = @[]

for i in 0..S.len:
  dp.add(newSeq[int](CHOKUDAI.len+1))

dp[0][0] = 1

for i in 0..S.len:
  for j in 0..CHOKUDAI.len:
    if i > 0:
      dp[i][j] = (dp[i][j] + dp[i-1][j]) mod MOD
    if i > 0 and j > 0 and S[i-1] == CHOKUDAI[j-1]:
      dp[i][j] = (dp[i][j] + dp[i-1][j-1]) mod MOD

echo dp[S.len][CHOKUDAI.len]
