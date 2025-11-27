import sys

data = sys.stdin.read().split()
N = int(data[0])
T = list(map(int, data[1:]))

stairs = [0] + T 

dp = [0] * (N + 1)

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp[1] = stairs[1] 
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) 

    for i in range(4, N + 1):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(dp[N])