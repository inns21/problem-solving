n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

cnt = 0
for i in range(len(n_list)): 
  start = 0
  end = len(n_list)-1
  target = n_list[i]
  while start < end:
    if start == i:
      start += 1
      continue
    if end == i:
      end -= 1
      continue
    if n_list[start] + n_list[end] < target:
      start += 1
    elif n_list[start] + n_list[end] > target:
      end -= 1
    else:
      cnt += 1
      break

print(cnt)
    