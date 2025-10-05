import sys
data = sys.stdin.read().split()

T = int(data[0])
N = list(map(int, data[1:]))

max_num = max(max(N), 4)

a, b, c = 1, 2, 4

dp = [0, a, b, c]
for i in range(4, max_num + 1):
    dp.append((dp[-1] + dp[-2] + dp[-3]) % 1000000009)

sys.stdout.write("\n".join(str(dp[n]) for n in N))
#-------
import sys
data = sys.stdin.read().split()

T = int(data[0])
N = list(map(int, data[1:]))

max_num = max(N)
max_num = max(max_num, 4)

dp = [0]*(max_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
    
for i in range(0, T):
    print(dp[N[i]])