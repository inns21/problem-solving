k = int(input())
n = int(input())

start_k = [chr(i+65) for i in range(k)]
result_k = list(input())

ladder = []
for i in range(n):
  ladder.append(input())

check = True
for i in range(n):
  if ladder[i][0] == '?':
    break
  for j in range(k-1):
    if ladder[i][j] == '-':
      temp = start_k[j]
      start_k[j] = start_k[j+1]
      start_k[j+1] = temp

for i in range(n-1,0,-1):
  if ladder[i][0] == '?':
    break
  for j in range(k-1):
    if ladder[i][j] == '-':
      temp = result_k[j]
      result_k[j] = result_k[j+1]
      result_k[j+1] = temp


result = ''
for i in range(k-1):
  if start_k[i] == result_k[i]:
    result += '*'
  elif start_k[i] == result_k[i+1]:
    result += '-'
    temp2 = start_k[i]
    start_k[i] = start_k[i+1]
    start_k[i+1] = temp2
  else:
    result = 'x'*(k-1)
    break

print(result)