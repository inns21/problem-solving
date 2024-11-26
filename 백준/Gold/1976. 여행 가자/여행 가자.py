n = int(input())
m = int(input())

connection = [{i + 1} for i in range(n)]
for i in range(n):
  cities = list(map(int, input().split()))
  for j in range(len(cities)):
    if cities[j] == 1:
      connection[i].add(j + 1)
      connection[j].add(i + 1)

total = set()
for i in range(n):
    for j in range(n):
        if connection[i] & connection[j]:  
            connection[i].update(connection[j])  
            connection[j].update(connection[i])  

plan = list(map(int, input().split()))
for group in connection:
    if set(plan).issubset(group): 
        print("YES")
        break
else:
    print("NO")