import sys
data = sys.stdin.read().split()

n = int(data[0])
nums = list(map(int, data[1:n+1]))

nums.sort(reverse=True)

isPrime = [True]*(nums[0]+1)
isPrime[0] = isPrime[1] = False
for i in range(2, int(nums[0]**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, nums[0]+1, i):
            isPrime[j] = False
cnt = 0 
for num in nums:
    if isPrime[num]:
        cnt += 1

print(cnt)
