n = int(input())
n_list = list(map(int, input().split()))

dp_plus = [0] * n
dp_minus = [0] * n
dp_plus[0] = 1
dp_minus[0] = 1
for i in range(1,n):
    dp_plus[i] = dp_plus[i-1] + 1 if n_list[i] >= n_list[i-1] else 1
    dp_minus[i] = dp_minus[i-1] + 1 if n_list[i] <= n_list[i-1] else 1
print(max(max(dp_minus), max(dp_plus)))