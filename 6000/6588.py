import sys
data = sys.stdin.read().split()

nums = list(map(int, data))
max_num = max(nums)

isPrime = [True]*(max_num+1)
isPrime[0] = isPrime[1] = False
for i in range(2, int(max_num**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, max_num+1, i):
            isPrime[j] = False
            
primes = [i for i in range(2, max_num + 1) if isPrime[i]]
prime_set = set(primes) # 이게 뭘까


for num in nums:
    if num == 0:
        break
    for p in primes:
        if p > num // 2:
            break
        if (num - p) in prime_set:
            print(f"{num} = {p} + {num - p}")
            break       