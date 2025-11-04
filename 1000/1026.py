import sys

def a(data):
    N = int(data[0])
    A , B = [], []
    for i in range(1, N+1):
       A.append(int(data[i])) 
       B.append(int(data[i+N]))
    
    A.sort()
    B.sort()
    
    S = 0
    for i in range(N):
        S += A[i] * B[N-1-i]
        
    return S
all_input_list = sys.stdin.read().split()    
print(a(all_input_list))