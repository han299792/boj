import sys 

def choose(S, A):
    para = -1
    for s in S:
        if s not in A:
            return s
        else:
            p = A.index(s)
            para = max(p, para)
    
    return A[para]

data = sys.stdin.read().split()

N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))
S = set()
cnt = 0 
for i in range(K):
    if A[i] in S:
        continue
    if len(S) < N:
        S.add(A[i])
        continue
    a = choose(S, A[i:])
    S.remove(a)
    S.add(A[i])
    cnt += 1
print(cnt)
    