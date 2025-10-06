import sys
data = sys.stdin.read().split()

N = int(data[0])
T = [0] + list(map(int, data[1:]))  

dp = [0] * (N + 1)

if N >= 1:
    dp[1] = T[1]
if N >= 2:
    dp[2] = T[1] + T[2]

for i in range(3, N + 1):
    dp[i] = max(
        dp[i-1],          
        dp[i-2] + T[i],    
        dp[i-3] + T[i-1] + T[i] 
    )

print(dp[N])
