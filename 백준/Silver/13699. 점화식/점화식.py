n = int(input())

dp = [0] * (n + 1)

if n == 0:  
    dp[0] = 1
elif n == 1:
    dp[1] = 1
elif n == 2:
    dp[2] = 2
elif n >= 3:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
print(dp[n])