count = 0
chess = list()

for i in range(8):
  col = input()
  for j in range(8):
    if i % 2 == 0:
      if j % 2 == 0:
        if col[j] == 'F':
          count += 1
    elif i % 2 != 0:
      if j % 2 != 0:
        if col[j] == 'F':
          count += 1
print(count)