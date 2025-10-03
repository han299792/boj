import sys
data = sys.stdin.read().split()

N  = int(data[0])
p = list(map(int, data[1:]))

max_num = max(5, N+1)
dp = [0] * max_num
dp[1] = p[0]
dp[2] = max(2*p[0], p[1])
dp[3] = max(3*p[0], p[0]+p[1], p[2])
dp[4] = max(4*p[0], 2*p[1], p[2]+p[0], p[3])

for i in range(5, N+1):
    p1 = dp[1] + dp[i-1]
    p2 = dp[2] + dp[i-2]
    p3 = dp[3] + dp[i-3]
    p4 = dp[4] + dp[i-4]
    dp[i] = max(p1, p2, p3, p4)

print(dp[N])
