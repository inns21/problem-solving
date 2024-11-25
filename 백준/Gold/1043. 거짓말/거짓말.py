n,m = map(int, input().split())
truth = set(list(map(int,input().split()))[1:])

party_list = []
for i in range(m):
  party = list(map(int, input().split()))[1:]
  party_list.append(party)

changed = True
while changed:
  changed = False
  for i in party_list:
    for j in i:
      if j in truth:
        before_len = len(truth)      
        truth.update(i)
        if before_len != len(truth):
          changed = True
  
count = m
for i in party_list:
  for j in i:
    if j in truth:
      count -= 1
      break

print(count)