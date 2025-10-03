import sys
data = sys.stdin.read().split()

N  = int(data[0])
p = list(map(int, data[1:]))

max_num = max(3, N+1)
dp = [0] * max_num
dp[1] = p[0]
dp[2] = min(2*p[0], p[1])

for i in range(3, N+1):
    min_cnt = p[i - 1]
    for j in range(1, i//2+1):
        para =  dp[j] + dp[i-j]
        min_cnt = min(para, min_cnt)
    dp[i] = min_cnt
        
print(dp[N])
