n = int(input())

n_list = [float(input()) for _ in range(n)]
dp = [0.0]*(n+1)
dp[0] = n_list[0]

for i in range(1,n):
  dp[i] = max(dp[i-1]*n_list[i], n_list[i])
  
print(f'{max(dp):.3f}')