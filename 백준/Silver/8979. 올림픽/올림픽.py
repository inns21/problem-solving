n, k = map(int, input().split())
countries = []

for _ in range(n):
  countries.append(list(map(int, input().split())))

countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

medals = []
for num,i in enumerate(countries):
  medals.insert(i[0]-1,num+1)

for i in range(1,n):
  if countries[i][1:] == countries[i-1][1:]:
    medals[i] = medals[i-1]
  else:
    medals[i] = medals[i-1] + 1
    
print(medals[k-1])
