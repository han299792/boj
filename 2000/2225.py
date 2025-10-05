import sys
data = sys.stdin.read().split()

N = int(data[0])
K = int(data[1])

#dp[k][n]: k 개의 정수를 골라서 합이 n이 되는 경우의 수
dp = [[0]*(N+1) for _ in range(K+1)]

for k in range(1, K+1):
    for n in range(N+1):
        if k == 1:
            dp[k][n] = 1
        else: 
            dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % 1000000000
        
print(dp[K][N])
        
        
    