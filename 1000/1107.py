import sys

N, M = map(int, sys.stdin.readline().split())

nums = []
for _ in range(N):

    row = list(map(int, sys.stdin.readline().split()))
    nums.append(row)