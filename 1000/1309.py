import sys

data = sys.stdin.read().split()

N = int(data[0])

dp = [[0]*3 for _ in range(N+1)]
dp[0][0], dp[0][1], dp[0][2] = 1,1,1

for n in range(1, N):
    dp[n][0] = (dp[n-1][0] + dp[n-1][1] + dp[n-1][2])%9901
    dp[n][1] = (dp[n-1][0] + dp[n-1][2])%9901
    dp[n][2] = (dp[n-1][0] + dp[n-1][1])%9901
    
result =(dp[N-1][0] + dp[N-1][1] + dp[N-1][2])%9901
print(result)
