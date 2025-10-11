import sys 

data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])
nums = list(map(int, data[2:]))
nums.sort()

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(0, N):
        s.append(nums[i])
        dfs()
        s.pop()
            
dfs()