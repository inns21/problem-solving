n = int(input())

w_list = []
for i in range(n):
  w_list.append(int(input()))

w_list.sort()
r_list = []
for i in range(n):
  r_list.append(w_list[i]*(n-i))
print(max(r_list))