from collections import deque

N = int(input())
card_tech = list(map(int, input().split()))
card_tech = card_tech[::-1]

card_list = [i+1 for i in range(N)]
result_list = deque()
for i in range(N):
  if card_tech[i] == 1:
    result_list.appendleft(card_list[i])
  elif card_tech[i] == 2:
    result_list.rotate(-1)
    result_list.appendleft(card_list[i])
    result_list.rotate(1)
  elif card_tech[i] == 3:
    result_list.append(card_list[i])
  
print(*result_list)
