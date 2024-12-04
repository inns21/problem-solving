n = int(input())

classroom = []
for i in range(n):
  student = list(map(int, input().split()))
  classroom.append(student)

new_list = []
for i in range(5):
  col = []
  for j in range(n):
    col.append(classroom[j][i])
  new_list.append(col)

result = {i+1:set() for i in range(n)}
for i in new_list:
  for j in range(len(i)):
    for k in range(len(i)):
      if i[j] == i[k] and j != k:
        result[j+1].add(k + 1)

max_count = max(len(v) for v in result.values())
student_num = [k for k, v in result.items() if len(v) == max_count]
print(student_num[0])

