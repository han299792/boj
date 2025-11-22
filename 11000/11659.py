N, M = map(int, input().split())
A = list(map(int, input().split()))

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + A[i]
    
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])