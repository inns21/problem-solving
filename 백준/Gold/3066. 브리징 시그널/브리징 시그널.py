T = int(input())

for _ in range(T):
  n = int(input())
  n_list = list()
  for i in range(n):
    n_list.append(int(input()))
  
  r_list = list()
  r_list.append(n_list[0])
  for i in range(1,n):
    if r_list[-1] < n_list[i]:
      r_list.append(n_list[i])
    else:
      start = 0
      end = len(r_list)-1
      while start <= end:
        mid = (start+end) // 2
        if r_list[mid] < n_list[i]:
          start = mid + 1
        else:
          end = mid - 1
      r_list[start] = n_list[i]
  
  print(len(r_list))