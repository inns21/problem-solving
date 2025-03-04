n = int(input())
n_list = list(map(int, input().split()))

s = int(input())
s_list = list()
for i in range(s):
  fm, num = map(int, input().split())
  if fm == 1:
    for j in range(num, n + 1, num):
      if n_list[j - 1] == 1:
        n_list[j - 1] = 0
      else:
        n_list[j - 1] = 1
  elif fm == 2:
    for k in range(num):
      if 0 < num - k and num + k <= n:
        if n_list[num - k - 1] == n_list[num + k - 1]:
          if n_list[num - k - 1] == 0:
            n_list[num - k - 1] = 1
            n_list[num + k - 1] = 1
          else:
            n_list[num - k - 1] = 0
            n_list[num + k - 1] = 0
        else:
          break

for i in range(0,n,20):
  print(*n_list[i:i+20])