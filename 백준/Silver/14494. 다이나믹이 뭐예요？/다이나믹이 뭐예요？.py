n,m = map(int, input().split())

dp = [[0]*n for i in range(m)]

for _ in range(m):
  dp[_][0] = 1

for _ in range(n):
  dp[0][_] = 1

for i in range(1,m):
  for j in range(1,n):
    dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + dp[i-1][j]
print(dp[m-1][n-1] % 1000000007)