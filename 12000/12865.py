import sys

data = sys.stdin.read().split()

N = int(data[0])
K = int(data[1])
w_list = []
v_list = []

for i in range(1,N+1):
    w_list.append(int(data[2*i]))
    v_list.append(int(data[2*i +1]))

dp = [0] * (K+1)
    
for i in range(N):
    weight = w_list[i]
    value = v_list[i]
    
    for w in range(K, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)

print(dp[K])