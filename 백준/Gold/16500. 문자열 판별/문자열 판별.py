s = input()
n = int(input())
a_list = list()
for _ in range(n):
  a_list.append(input())

result = [False]*(len(s)+1)
result[0] = True

for i in range(len(s)):
  if result[i]:
    for j in a_list:
      if s[i:i+len(j)] == j:
        result[i+len(j)] = True
  

if result[len(s)]:
  print(1)
else:
  print(0)
    