n = int(input())
nums = list(map(int, input().split()))

def next_permutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(nums) - 1
    while nums[j] <= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]

    nums[i:] = nums[len(nums)-1:i-1:-1]
    return True

if next_permutation(nums):
    print(*nums)
else:
    print(-1)
