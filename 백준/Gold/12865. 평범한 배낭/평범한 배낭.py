n,k = map(int, input().split())

n_list = list()
for i in range(n):
  w,v = map(int, input().split())
  n_list.append([w,v])

dp = [0 for _ in range(k+1)]
for w, v in n_list:  
  for j in range(k, w - 1, -1):
      dp[j] = max(dp[j], dp[j - w] + v)
print(dp[k])