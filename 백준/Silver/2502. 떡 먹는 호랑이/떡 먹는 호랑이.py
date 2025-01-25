d,k = map(int, input().split())

dp = ['']*(d+1)
dp[1] = 'a'
dp[2] = 'b'

for i in range(3,d+1):
  dp[i] = dp[i-1] + dp[i-2]

a_cnt = dp[d].count('a')
b_cnt = dp[d].count('b')

a_list = []
b_list = []
for i in range(1,k):
  if len(a_list) != 0 and len(b_list) != 0:
    break
  for j in range(i,k):
    if a_cnt*i + b_cnt*j == k:
      a_list.append(i)
      b_list.append(j)
      break
  

print(a_list[0])
print(b_list[0])
  
