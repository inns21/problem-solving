n,c = map(int, input().split())

n_list = list()
for i in range(n):
  n_list.append(int(input()))

n_list.sort()

min = 1
max = n_list[-1] - n_list[0]

while(min <= max):
  mid = (min+max) // 2
  start = n_list[0]
  cnt = 1
  for i in range(1,len(n_list)):
    if n_list[i] - start >= mid:
      cnt += 1
      start = n_list[i]
  if cnt >= c:
    min = mid + 1
  else:
    max = mid - 1

print(max)
      