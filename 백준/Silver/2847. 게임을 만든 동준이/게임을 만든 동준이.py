n = int(input())

scores = []
for i in range(n):
  scores.append(int(input()))

result = 0
level = scores[-1]-1
for i in range(n-2,-1,-1):
  if scores[i] > level:
    result += scores[i] - level
  elif scores[i] < level:
    level = scores[i]
  level -= 1

print(result)