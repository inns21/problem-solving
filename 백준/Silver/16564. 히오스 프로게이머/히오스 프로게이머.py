n, k = map(int,input().split())

characters = []
for i in range(n):
  character = int(input())
  characters.append(character)

start = min(characters)
end = 1000000001
while start <= end:
  mid = (start+end) // 2

  levelup = 0
  for i in range(len(characters)):
    if characters[i] >= mid :
      continue
    levelup += abs(mid - characters[i])
  if levelup <= k:
    start = mid + 1
  else:
    end = mid - 1

print(end)