import sys
input = sys.stdin.readline 

n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

dp_min = n_list[0][:]
dp_max = n_list[0][:]

for i in range(1, n):
    prev_min = dp_min[:]
    prev_max = dp_max[:]

    dp_min[0] = min(prev_min[0], prev_min[1]) + n_list[i][0]
    dp_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + n_list[i][1]
    dp_min[2] = min(prev_min[1], prev_min[2]) + n_list[i][2]

    dp_max[0] = max(prev_max[0], prev_max[1]) + n_list[i][0]
    dp_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + n_list[i][1]
    dp_max[2] = max(prev_max[1], prev_max[2]) + n_list[i][2]


print(max(dp_max), min(dp_min))
