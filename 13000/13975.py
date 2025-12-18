import sys, heapq

input=sys.stdin.readline

def optimal(K,P):
    ans = 0 
    heapq.heapify(P)
    while len(P)>1:
        a, b = heapq.heappop(P), heapq.heappop(P)
        c = a+b
        ans += c
        heapq.heappush(P, c)
        
    return ans

T=int(input())
for _ in range(T):
    K=int(input())
    P=list(map(int, input().split()))
    print(optimal(K, P))