import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

prefix_sum = [[0] * 26 for _ in range(len(S) + 1)]


for i in range(1, len(S) + 1):
    for j in range(26):
        prefix_sum[i][j] = prefix_sum[i-1][j]
    prefix_sum[i][ord(S[i-1]) - ord('a')] += 1

for _ in range(q):
    alpha, l, r = sys.stdin.readline().split()
    l, r = int(l), int(r)
    result = prefix_sum[r+1][ord(alpha) - ord('a')] - prefix_sum[l][ord(alpha) - ord('a')]
    print(result)
