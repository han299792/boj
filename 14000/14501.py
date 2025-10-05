from numbers import Number
import sys
import math
data = sys.stdin.read().split()

N = int(data[0])
T = [0]
P = [0]
for i in range(1, N+1):
    T.append(int(data[2*i -1]))
    P.append(int(data[2*i]))
    
dp = [[0,0] for _ in range(N+1)]
result = 0
for i in range(1, N+1):
    dp[i][0] = T[i] + i - 1


for i in range(1, N+1):
    if dp[i][0] < N +1:
        dp[i][1] = P[i]
        for j in range(1,i):
            if dp[j][0] < i:
                dp[i][1] = max(dp[i][1], dp[j][1] + P[i])
                result = max(result, dp[i][1])
    result = max(result, dp[i][1])
        
     
print(result)

# 더 괜찮은 풀이
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])

T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i] = int(data[2 * i - 1])
    P[i] = int(data[2 * i])

dp = [0] * (N + 2)  # dp[i] = i번째 날까지 얻을 수 있는 최대 수익

for i in range(1, N + 1):
    # i번째 상담을 안 하는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])
    # i번째 상담을 하는 경우
    if i + T[i] <= N + 1:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(max(dp))

