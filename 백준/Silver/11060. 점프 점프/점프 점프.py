n = int(input())
jumps = list(map(int, input().split()))

dp = [1000] * n
dp[0] = 0
for i in range(n):
    for j in range(1, jumps[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[n-1] if dp[n-1] != 1000 else -1)
