import sys
input = sys.stdin.readline 

T = int(input()) 

for _ in range(T):
    N = int(input()) 
    
    ranks = [0] * (N + 1)
    
    for i in range(N):
        a1, a2 = map(int, input().split())
        ranks[a1] = a2
        
    cnt = 1
    min_rank = ranks[1]
    
    for i in range(2, N+1):
        if ranks[i] < min_rank:
            min_rank = ranks[i]
            cnt += 1
            
    print(cnt)
