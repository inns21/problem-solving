n = int(input())
s = list(map(int, input().split()))

result_list = {0}

for num in s:
  new_sums = set()
  for i in result_list:
    new_sums.add(i + num)
  result_list.update(new_sums)

result = 1
while result in result_list:
  result += 1

print(result)