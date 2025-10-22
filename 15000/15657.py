import sys
data = sys.stdin.read().split()

N, M = int(data[0]), int(data[1])
nums = list(map(int, data[2:]))
nums.sort()

s = []

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N):
        s.append(nums[i])
        dfs(i)
        s.pop() 
dfs(0)