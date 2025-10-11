import sys 

data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            
dfs()