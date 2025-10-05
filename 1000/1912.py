import sys
data = sys.stdin.read().split()

N = int(data[0])
dp = [0]*N
for i in range(1, N):
    

print(max(dp))
