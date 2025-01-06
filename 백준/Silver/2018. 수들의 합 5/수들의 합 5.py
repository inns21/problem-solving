n = int(input())

result = 1
for i in range(1,(n//2)+1):
  hap = i
  for j in range(i+1,n):
    hap += j
    if hap == n:
      result += 1
      break
    elif hap > n:
      break
    
print(result)