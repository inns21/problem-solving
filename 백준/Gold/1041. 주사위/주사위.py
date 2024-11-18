n = int(input())
dice = list(map(int, input().split()))

mirror = {0:5,1:4, 2:3, 3:2, 4:1, 5:0}

thr = 4
two = 4*(n-1) + 4*(n-2)
one = ((n-2)**2)*5 + 4*(n-2)
total = 0
if n == 1:
  total = sum(dice) - max(dice)
else:
  total += one*min(dice)

  two_list = []
  for i in range(6):
    for j in range(6):
      if i != j and j != mirror[i]:
        two_list.append(dice[i]+dice[j])

  thr_list = []
  # 012 / 013 / 025 / 034 / 135 / 125 / 245 / 345
  for i in range(6):
    for j in range(6):
      if i == j or j == mirror[i]:
        continue
      for k in range(6):
        if k in (i,j) or k == mirror[i] or k == mirror[j]:
          continue
        thr_list.append(dice[i]+dice[j]+dice[k])

  total += two*min(two_list)
  total += thr*min(thr_list)
print(total)  