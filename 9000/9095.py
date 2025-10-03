import sys
data = sys.stdin.read().split()

nums = list(map(int, data))

def count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return count(n - 3) + count(n - 2) + count(n - 1) 
for i in range(1, nums[0]+1):
    print(count(nums[i]))