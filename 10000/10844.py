import sys
data = sys.stdin.read().split()

N = int(data[0])

dp = [[0]*2 for _ in range(N+1)]
dp[1][1] = 1
dp[1][0] = 0

for i in range(2, N+1):
    for j in range(0,2):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j]
        if j == 1:
            dp[i][j] = dp[i-1][j-1]
            
print(dp[N][0]+dp[N][1])