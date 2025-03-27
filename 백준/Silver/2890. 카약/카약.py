r,c = map(int,input().split())

kayaks = list()
for i in range(r):
  kayaks.append(list(input().strip()))

dist = []
for i in kayaks:
  for idx,k in enumerate(range(c)):
    if i[idx].isdigit():
      dist.append((int(i[idx]),idx))
      break

dist.sort(key=lambda x: x[1], reverse=True)

ranks = {}
rank = 1
temp = dist[0][1]
for num, _ in dist:
  if temp == _:
    ranks[num] = rank
  else:
    rank += 1
    ranks[num] = rank
  temp = _

sorted_ranks = sorted(ranks.items(), key=lambda x: x[0]) 
for _, rank in sorted_ranks:
    print(rank)