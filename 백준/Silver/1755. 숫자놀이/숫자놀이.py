alpha ={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

m,n = map(int, input().split())
result = {}
for i in range(m, n+1):
  s = str(i)
  r = ''
  for j in s:
    r += alpha[j]
  result[s] = r

result = sorted(result.items(), key= lambda x: x[1])

for idx, value in enumerate(result, start=1):
    print(value[0], end=' ')
    if idx % 10 == 0:  
        print()
