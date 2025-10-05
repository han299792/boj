import sys
data = sys.stdin.read().split()

N = int(data[0])
A = list(map(int, data[1:]))

dp = [1]*N
B = [0]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:    
            dp[i][0] = max(dp[j][0]+1, dp[i][0])
            n = dp[i][0]
            dp[i][n]
            
print(max(dp))
print(dp[1:])

