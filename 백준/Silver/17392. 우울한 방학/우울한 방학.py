n,m = map(int, input().split())
n_list = list(map(int, input().split()))

happy = sum(n_list) + len(n_list)
if happy >= m:
  print(0)
else:
  gloomy = m - happy
  result = 0
  i = 0
  for i in range(1,gloomy // (len(n_list)+1)+1):
    result += (len(n_list)+1)*i**2
  result += (gloomy % (len(n_list)+1))*(i+1)**2
  print(result)
    