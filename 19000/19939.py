

def a(data):
    N, K = map(int, data)

    pivot = (K+1)*K//2

    if N < pivot:
        return -1
    n = N-pivot
    
    cnt = 0
     
    if n > K:
        cnt += n // K
        n = n%K
    if n == 0:
        return K -1  
    return  K -1 + 1


print(a(input().split()))