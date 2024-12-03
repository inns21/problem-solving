n = int(input())

cut = 0
paper = 1
while True:
  if paper < n:
    if cut + paper > n:
      cut += (n + 1) // 2
      break
    cut += paper
    paper *= 2
  else:
    break
print(cut)
