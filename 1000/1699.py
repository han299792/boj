from numbers import Number
import sys
import math
data = sys.stdin.read().split()

N = int(data[0])
dp = [float('inf')] * (N + 1)
dp[0] = 0
for i in range(1, N+1):
    # if int(math.sqrt(i)) ** 2 == i:
    #     dp[i] = 1
    rootI = int(i ** 0.5)
    for j in range (1, rootI+1):
        dp[i] = min(dp[i], dp[i-j**2] +1)
    
print(dp[N])
