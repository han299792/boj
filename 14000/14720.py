import sys

data = sys.stdin.read().split()
N = int(data[0])
nums = list(map(int, data[1:]))

cnt = 0

for n in nums:
    if cnt%3 == n:
        cnt += 1

print(cnt)
        