import sys
data = sys.stdin.read().split()

A,B = data[0], data[1]
a, b = len(A), len(B)
dp = [[""]*(b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
            
print(len(dp[a][b]))
print(dp[a][b])