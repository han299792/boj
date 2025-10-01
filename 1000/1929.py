import sys
data = sys.stdin.read().split()

m = int(data[0])
n = int(data[1])

isPrime = [True] * (n+1)
isPrime[0] = isPrime[1] = False
cnt = 0
for i in range(2, int(n**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, n+1, i):
            isPrime[j] = False
            
for i in range(m, n+1):
    if isPrime[i]:
        print(i)
