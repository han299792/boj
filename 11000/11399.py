import sys 

data = sys.stdin.read().split()
N = int(data[0])
P = list(map(int, data[1:]))
P.sort()
sum = 0 
for i in range(N):
    sum += P[i]*(N-i)


print(sum)