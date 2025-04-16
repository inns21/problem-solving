import sys

n = int(input())
n_list = list(map(int, input().split()))

r_list = [0 for _ in range(n+1)]
hap = 0
for i in range(n):
    hap += n_list[i]
    r_list[i+1] = hap

a = int(input())
for _ in range(a):
    i,j = map(int, sys.stdin.readline().split())
    print(r_list[j]-r_list[i-1])