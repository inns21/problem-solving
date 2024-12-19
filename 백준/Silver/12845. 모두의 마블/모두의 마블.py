n = int(input())
l = list(map(int, input().split()))

max_level = max(l)
total = 0

for card in l:
    if card != max_level:
        total += max_level + card

if l.count(max_level) == 1:
  print(total)
else:
  print(total + max_level*2*(l.count(max_level)-1))