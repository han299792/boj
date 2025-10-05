import sys

data = sys.stdin.read().split()

N = int(data[0])
result = 1

for i in range(1, N+10):
    result = result*i
for j in range(1, N+1):
    result = result // j   
for k in range(1, 10):
    result = result // k
print(result%10007)