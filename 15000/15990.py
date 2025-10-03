import sys
data = sys.stdin.read().split()

N = int(data[0])
nums = list(map(int, data[1:]))

max_num = max(nums)
max_num = max(4,max_num)
dp = [[0]*4 for _ in range(max_num+1)]

dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, max_num+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3])%1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3])%1000000009
    dp[i][3] = (dp[i-3][1] + dp[i-3][2])%1000000009

    
out = []
for n in nums:
    out.append(str((dp[n][1] + dp[n][2] + dp[n][3]) % 1000000009))
sys.stdout.write("\n".join(out))
