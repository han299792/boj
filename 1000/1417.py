import sys
data = sys.stdin.read().split()

N = int(data[0])
A = list(map(int, data[1:]))

S = sum(A)
K = S//N + 1

ans = K - A[0] if K > A[0] else 0
print(ans)