def find_num(x, n, nums):
  if n == len(x):
      nums.append(int(''.join(x)))  
      return
  for i in range(n, len(x)):
      x[n], x[i] = x[i], x[n]  
      find_num(x, n + 1, nums)
      x[n], x[i] = x[i], x[n] 


x = list(input()) 
nums = []
find_num(x, 0, nums)
nums = list(set(nums))
nums.sort()
r_index = nums.index(int(''.join(x)))
print(nums[r_index+1] if r_index+1 < len(nums) else 0)