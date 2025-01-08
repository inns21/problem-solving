h, w, x, y = map(int, input().split())

b = []
for _ in range(h + x):
    b.append(list(map(int, input().split())))

a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
      if i >= x and j >= y:
          a[i][j] = b[i][j] - a[i - x][j - y]
      else:
          a[i][j] = b[i][j]


for row in a:
    print(*row)
